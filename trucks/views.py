from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from trucks.models import Trucks
from .forms import TruckForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trucks:homepage')  # Redirect to the same page to clear the form
    else:
        form = TruckForm()

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

    truckForm = TruckForm()
    context = {
        'trucks': trucks,
        'form': truckForm
    }
    return render(request, 'trucks/index.html', context)


def truckById(request, id):
    truck = get_object_or_404(Trucks, id=id)
    return render(request, 'trucks/truck.html', {'truck': truck})


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