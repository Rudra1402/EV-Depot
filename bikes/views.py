from django.shortcuts import render
from django.http import HttpResponse

from bikes.models import Bikes
# Create your views here.
def index(request):
    bikes = Bikes.objects.all()
    context = {
        'bikes': bikes
    }
    return render(request,'index.html', context)