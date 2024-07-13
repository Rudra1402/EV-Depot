from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from bikes.models import Bikes
from .forms import BikeForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
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
        'form': bikeForm
    }
    return render(request,'index.html', context)

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