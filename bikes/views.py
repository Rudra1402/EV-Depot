from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from bikes.models import Bikes
from .forms import BikeForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to the same page to clear the form
    else:
        form = BikeForm()

    bikes = Bikes.objects.all().order_by('-createdAt')
    bikeForm = BikeForm()
    context = {
        'bikes': bikes,
        'form': bikeForm
    }
    return render(request,'index.html', context)

def bikeById(request, id):
    bike = get_object_or_404(Bikes, id=id)
    return render(request, 'bike.html', {'bike': bike})