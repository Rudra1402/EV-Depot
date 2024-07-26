from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.urls import reverse

from trucks.models import Trucks
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
                    truck.user = Buyer.objects.get(pk=7)
                    print(Buyer.objects.get(pk=7))

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
            'trucks': trucks,
            'form': truckForm,
            'visit_counts': request.visit_counts,
            'most_visited_app': max(request.visit_counts, key=request.visit_counts.get)
        }
        return render(request, 'trucks/index.html', context)
    except Exception as e:
        print(str(e))


def truckById(request, id):
    truck = get_object_or_404(Trucks, id=id)
    return render(request, 'trucks/truck.html', {'truck': truck})

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
        'trucks': trucks
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