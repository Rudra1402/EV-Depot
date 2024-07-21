from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from users.models import Buyer
from .utils import upload_image_to_firebase

from bikes.models import Bikes
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
                    bike.user = Buyer.objects.get(pk=4)

                form.save()
                return redirect('bikes:homepage')  # Redirect to the same page to clear the form
        else:
            form = BikeForm()

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

        bikeForm = BikeForm()
        context = {
            'bikes': bikes,
            'form': bikeForm,
            'visit_counts': request.visit_counts,
            'most_visited_app': max(request.visit_counts, key=request.visit_counts.get)
        }
        return render(request,'index.html', context)
    except Exception as e:
        print(str(e))

def bikeById(request, id):
    bike = get_object_or_404(Bikes, id=id)
    return render(request, 'bike.html', {'bike': bike})

def delete_bike(request, id):
    if request.method == 'DELETE':
        print(f"Received DELETE request for bike ID {id}")
        bike = get_object_or_404(Bikes, pk=id)
        bike.delete()
        return JsonResponse({"message": "Bike deleted successfully."}, status=200)
    else:
        print(f"Received {request.method} request, only DELETE is allowed")
        raise Http404("Only DELETE method is allowed")


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
        'bikes': bikes
    }
    return render(request, 'index.html', context)