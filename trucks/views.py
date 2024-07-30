from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods, require_POST
from django.db.models import Q, Avg
from django.urls import reverse

from trucks.models import Trucks, RatingT
from .forms import TruckForm
from users.models import Buyer
from .utils import upload_image_to_firebase

# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            form = TruckForm(request.POST, request.FILES)
            print(request.POST, request.FILES)
            if form.is_valid():
                truck = form.save(commit=False)

                if 'image' in request.FILES:
                    image = request.FILES['image']
                    image_url = upload_image_to_firebase(image, 'truck_images')
                    truck.image = image_url
                    user = Buyer.objects.get(username=request.user)
                    truck.user = Buyer.objects.get(pk=user.id)

                form.save()
                return redirect('trucks:homepage')  # Redirect to the same page to clear the form
        else:
            form = TruckForm()

        trucks = Trucks.objects.filter(purchasedBy__isnull=True)
        # trucks = Trucks.objects.all()

        latest = request.GET.get('latest')
        if latest:
            trucks = trucks.order_by('-createdAt')

        sort = request.GET.get('sort')
        if sort == 'name':
            trucks = trucks.order_by('name')

        query = request.GET.get('query')
        if query:
            trucks = trucks.filter(name__icontains=query)

        truckForm = TruckForm()
        context = {
            'trucks': trucks.annotate(average_rating=Avg('ratings__rating')),
            'form': truckForm,
            'visit_counts': request.visit_counts,
            'most_visited_app': max(request.visit_counts, key=request.visit_counts.get)
        }
        return render(request, 'trucks/index.html', context)
    except Exception as e:
        print(str(e))


def truckById(request, id):
    truck = get_object_or_404(Trucks, id=id)
    user_rating = None
    buyer = get_object_or_404(Buyer, username=request.user)
    if request.user.is_authenticated:
        user_rating = RatingT.objects.filter(truck=truck, user=buyer).first()
    return render(request, 'trucks/truck.html', {'truck': truck, 'user_rating': user_rating})
@login_required
@require_POST
def rate_truck(request, truck_id):
    truck = get_object_or_404(Trucks, id=truck_id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        if rating_value:
            rating_value = int(rating_value)
            # Ensure rating is between 1 and 5
            if 1 <= rating_value <= 5:
                buyer = get_object_or_404(Buyer, username=request.user)
                RatingT.objects.update_or_create(
                    truck=truck,
                    user=buyer,
                    defaults={'rating': rating_value}
                )
                return redirect('trucks:homepage')
    return JsonResponse({'success': False, 'message': 'Invalid rating'}, status=400)

def edit_truck(request, id):
    truck = get_object_or_404(Trucks, id=id)

    if request.method == 'POST':
        form = TruckForm(request.POST, request.FILES, instance=truck)
        if form.is_valid():
            if 'image' in request.FILES:
                image = request.FILES['image']
                image_url = upload_image_to_firebase(image, 'truck_images')
                truck.image = image_url
            form.save()
            return redirect('trucks:homepage')
    else:
        form = TruckForm(instance=truck)
        form.fields['image'].initial = None

    context = {
        'form': form,
        'truck': truck,
    }
    return render(request, 'trucks/edit_truck.html', context)

def delete_truck(request, id):
    if request.method == 'DELETE':
        print(f"Received DELETE request for truck ID {id}")
        truck = get_object_or_404(Trucks, pk=id)
        truck.delete()
        return JsonResponse({"message": "Truck deleted successfully."}, status=200)
    else:
        print(f"Received {request.method} request, only DELETE is allowed")
        raise Http404("Only DELETE method is allowed")


def truck_list(request):
    trucks = Trucks.objects.all()

    latest = request.GET.get('latest')
    if latest:
        trucks = trucks.order_by('-createdAt')

    sort = request.GET.get('sort')
    if sort == 'name':
        trucks = trucks.order_by('name')

    query = request.GET.get('query')
    if query:
        trucks = trucks.filter(name__icontains=query)

    context = {
        'trucks': trucks.annotate(average_rating=Avg('ratings__rating'))
    }
    return render(request, 'trucks/index.html', context)

def purchase_truck(request, truck_id):
    truck = get_object_or_404(Trucks, id=truck_id)
    owner = truck.user
    return render(request, 'purchase_truck.html', {'truck': truck, 'owner': owner})

def complete_purchase(request, truck_id):
    truck = get_object_or_404(Trucks, id=truck_id)
    buyer = Buyer.objects.get(username=request.user)
    owner = truck.user

    # Allocate points
    buyer.points += 100  # or any logic to calculate points
    buyer.save()
    owner.points += 50  # or any logic to calculate points
    owner.save()

    # Mark the truck as purchased
    truck.purchasedBy = buyer
    truck.save()

    return redirect(reverse('trucks:homepage'))