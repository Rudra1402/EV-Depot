from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
# Create your views here.
from cars.models import Cars
from .forms import CarForm


def carindex(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:homepage')  # Redirect to the same page to clear the form
    else:
        form = CarForm()

    cars = Cars.objects.all().order_by('-createdAt')
    car_form = CarForm()
    context = {
        'cars': cars,
        'form': car_form,
        'visit_counts': request.visit_counts,
        'most_visited_app': max(request.visit_counts, key=request.visit_counts.get)
    }
    return render(request, 'cars/carindex.html', context)


def carById(request, id):
    car = get_object_or_404(Cars, id=id)
    return render(request, 'cars/car.html', {'car': car})


def deleteCar(request, id):
    if request.method == 'DELETE':
        print(f"Received DELETE request for car ID {id}")
        car = get_object_or_404(Cars, pk=id)
        car.delete()
        return JsonResponse({"message": "Bike deleted successfully."}, status=200)
    else:
        print(f"Received {request.method} request, only DELETE is allowed")
        raise Http404("Only DELETE method is allowed")
