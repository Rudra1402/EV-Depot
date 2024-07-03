from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from bikes.models import Bikes
# Create your views here.
def index(request):
    # bikes = Bikes.objects.all()
    bikes = [
        {
            "name":"Speedster 500",
            "companyName":"FastBikes Inc.",
            "modelType":"road",
            "manufacturingYear":2023,
            "price":1299.99,
            "description":"A high-performance road bike designed for speed and efficiency.",
            "image":"https://media.istockphoto.com/id/1415317051/photo/black-electric-bike-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=KLlFOJEFWPpSDe9TWB2kqGKS2GuvNp_mhe7y53wnIfA=",
            "isNew":True,
            "createdAt": datetime.now()
        },
        {
            "name":"Speedster 500",
            "companyName":"FastBikes Inc.",
            "modelType":"road",
            "manufacturingYear":2023,
            "price":1299.99,
            "description":"A high-performance road bike designed for speed and efficiency.",
            "image":"https://media.istockphoto.com/id/1415317051/photo/black-electric-bike-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=KLlFOJEFWPpSDe9TWB2kqGKS2GuvNp_mhe7y53wnIfA=",
            "isNew":True,
            "createdAt": datetime.now()
        }
    ]
    context = {
        'bikes': bikes
    }
    return render(request,'index.html', context)