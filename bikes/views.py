from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.urls import reverse

from users.models import Buyer
from .utils import upload_image_to_firebase

from bikes.models import Bikes, Rating
from .forms import BikeForm


# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            form = BikeForm(request.POST, request.FILES)
            print(request.POST, request.FILES)
            if form.is_valid():
                bike = form.save(commit=False)

                if 'image' in request.FILES:
                    image = request.FILES['image']
                    image_url = upload_image_to_firebase(image, 'bike_images')
                    bike.image = image_url
                    user = Buyer.objects.get(username=request.user)
                    bike.user = Buyer.objects.get(pk=user.id)

                form.save()
                return redirect('bikes:homepage')  # Redirect to the same page to clear the form
        else:
            form = BikeForm()

        bikes = Bikes.objects.filter(purchasedBy__isnull=True)

        latest = request.GET.get('latest')
        if latest:
            bikes = bikes.order_by('-createdAt')

        sort = request.GET.get('sort')
        if sort == 'name':
            bikes = bikes.order_by('name')

        query = request.GET.get('query')
        if query:
            bikes = bikes.filter(name__icontains=query)

        bikeForm = BikeForm()
        context = {
            'bikes': bikes.annotate(average_rating=Avg('ratings__rating')),
            'form': bikeForm,
            'visit_counts': request.visit_counts,
            'most_visited_app': max(request.visit_counts, key=request.visit_counts.get)
        }
        return render(request, 'index.html', context)
    except Exception as e:
        print(str(e))


def bikeById(request, id):
    bike = get_object_or_404(Bikes, id=id)
    user_rating = None
    buyer = get_object_or_404(Buyer, username=request.user)
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(bike=bike, user=buyer).first()
    return render(request, 'bike.html', {'bike': bike, 'user_rating': user_rating})


def delete_bike(request, id):
    if request.method == 'DELETE':
        print(f"Received DELETE request for bike ID {id}")
        bike = get_object_or_404(Bikes, pk=id)
        bike.delete()
        return JsonResponse({"message": "Bike deleted successfully."}, status=200)
    else:
        print(f"Received {request.method} request, only DELETE is allowed")
        raise Http404("Only DELETE method is allowed")


@login_required
@require_POST
def rate_bike(request, bike_id):
    bike = get_object_or_404(Bikes, id=bike_id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        if rating_value:
            rating_value = int(rating_value)
            # Ensure rating is between 1 and 5
            if 1 <= rating_value <= 5:
                buyer = get_object_or_404(Buyer, username=request.user)
                Rating.objects.update_or_create(
                    bike=bike,
                    user=buyer,
                    defaults={'rating': rating_value}
                )
                return redirect('bikes:homepage')
    return JsonResponse({'success': False, 'message': 'Invalid rating'}, status=400)


def edit_bike(request, id):
    bike = get_object_or_404(Bikes, id=id)

    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES, instance=bike)
        if form.is_valid():
            if 'image' in request.FILES:
                image = request.FILES['image']
                image_url = upload_image_to_firebase(image, 'bike_images')
                bike.image = image_url
            form.save()
            return redirect('bikes:homepage')
    else:
        form = BikeForm(instance=bike)
        form.fields['image'].initial = None

    context = {
        'form': form,
        'bike': bike,
    }
    return render(request, 'edit_bike.html', context)


def bike_list(request):
    bikes = Bikes.objects.all()

    latest = request.GET.get('latest')
    if latest:
        bikes = bikes.order_by('-createdAt')

    sort = request.GET.get('sort')
    if sort == 'name':
        bikes = bikes.order_by('name')

    query = request.GET.get('query')
    if query:
        bikes = bikes.filter(name__icontains=query)

    context = {
        'bikes': bikes.annotate(average_rating=Avg('ratings__rating'))
    }
    return render(request, 'index.html', context)


# @login_required
def purchase_bike(request, bike_id):
    bike = get_object_or_404(Bikes, id=bike_id)
    owner = bike.user
    return render(request, 'purchase_bike.html', {'bike': bike, 'owner': owner})


# @login_required
def complete_purchase(request, bike_id):
    bike = get_object_or_404(Bikes, id=bike_id)
    buyer = Buyer.objects.get(username=request.user)
    owner = bike.user

    # Allocate points
    buyer.points += 100  # or any logic to calculate points
    buyer.save()
    owner.points += 50  # or any logic to calculate points
    owner.save()

    # Mark the bike as purchased
    bike.purchasedBy = buyer
    bike.save()


    return redirect(reverse('bikes:homepage'))  # or any page you want to redirect to




