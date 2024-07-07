from datetime import datetime, timedelta
from django.shortcuts import render, redirect
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
    # bikes = [
    #     {
    #         "name": "Speedster 500",
    #         "companyName": "FastBikes Inc.",
    #         "modelType": "road",
    #         "manufacturingYear": 2023,
    #         "price": 1299.99,
    #         "description": "A high-performance road bike designed for speed and efficiency. The Speedster 500 features a lightweight aluminum frame, carbon fork, and high-quality components, making it the perfect choice for competitive cyclists and enthusiasts alike. With its aerodynamic design and precise handling, you'll experience unmatched performance on every ride.",
    #         "image": "https://media.istockphoto.com/id/1415317051/photo/black-electric-bike-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=KLlFOJEFWPpSDe9TWB2kqGKS2GuvNp_mhe7y53wnIfA=",
    #         "isNew": True,
    #         "createdAt": datetime.now() - timedelta(hours=2 ,minutes=45)
    #     },
    #     {
    #         "name": "Mountain Master",
    #         "companyName": "TrailBlazers Co.",
    #         "modelType": "mountain",
    #         "manufacturingYear": 2022,
    #         "price": 1599.99,
    #         "description": "The Mountain Master is built to conquer the toughest terrains with ease. Featuring a robust frame, advanced suspension system, and durable components, this mountain bike is perfect for off-road adventures. Whether you're tackling steep climbs or rocky descents, the Mountain Master delivers exceptional performance and control.",
    #         "image": "https://i.zst.com.br/thumbs/12/3f/1d/1579849623.jpg",
    #         "isNew": True,
    #         "createdAt": datetime.now() - timedelta(hours=1 ,minutes=30)
    #     },
    #     {
    #         "name": "Hybrid Hero",
    #         "companyName": "EcoRides Ltd.",
    #         "modelType": "hybrid",
    #         "manufacturingYear": 2021,
    #         "price": 999.99,
    #         "description": "Combining the best features of road and mountain bikes, the Hybrid Hero is the ultimate all-purpose bike. Its versatile design allows for smooth commuting on city streets and confident handling on light trails. With a comfortable upright riding position and reliable components, the Hybrid Hero is perfect for riders seeking a balanced, efficient ride.",
    #         "image": "https://admin.ecoride.se/wp-content/uploads/2020/10/thumbnails/tripper-hs-h-9-svart-1600x900.png",
    #         "isNew": False,
    #         "createdAt": datetime.now() - timedelta(weeks=1 ,days=2)
    #     },
    #     {
    #         "name": "Cruiser Classic",
    #         "companyName": "BeachBreeze Bikes",
    #         "modelType": "cruiser",
    #         "manufacturingYear": 2020,
    #         "price": 799.99,
    #         "description": "Experience the joy of relaxed riding with the Cruiser Classic. This bike is designed for leisurely rides along the beach or around town. Its comfortable saddle, wide handlebars, and smooth-rolling tires ensure a laid-back and enjoyable experience. With its retro-inspired design, the Cruiser Classic is as stylish as it is comfortable.",
    #         "image": "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1665688244-16-780-7111-simi-2022-21383-teal-web-profile.png?crop=1xw:1.00xh;center,top&resize=980:*",
    #         "isNew": False,
    #         "createdAt": datetime.now()
    #     },
    #     {
    #         "name": "Road Racer",
    #         "companyName": "SpeedyWheels",
    #         "modelType": "road",
    #         "manufacturingYear": 2022,
    #         "price": 1499.99,
    #         "description": "The Road Racer is engineered for speed and performance. Its aerodynamic frame, lightweight construction, and precision components make it a top choice for competitive cyclists and serious enthusiasts. Whether you're training for a race or enjoying a long-distance ride, the Road Racer offers unmatched efficiency and responsiveness.",
    #         "image": "https://media.theradavist.com/uploads/2022/03/DSC09388.jpeg?w=1400&quality=75",
    #         "isNew": True,
    #         "createdAt": datetime.now()
    #     },
    #     {
    #         "name": "Trail Tracker",
    #         "companyName": "AdventureCycles",
    #         "modelType": "mountain",
    #         "manufacturingYear": 2023,
    #         "price": 1799.99,
    #         "description": "Designed for the thrill-seekers, the Trail Tracker is perfect for tackling rugged trails and challenging terrains. Its sturdy frame, advanced suspension, and high-quality components ensure a smooth and controlled ride, even in the roughest conditions. With the Trail Tracker, every off-road adventure becomes an exhilarating experience.",
    #         "image": "https://www.intheholegolf.com/img/pedego-electric-bicycles/pedego-trail-tracker-fat-tire-electric-bike-black-lime-2.jpg",
    #         "isNew": True,
    #         "createdAt": datetime.now()
    #     },
    #     {
    #         "name": "City Commuter",
    #         "companyName": "UrbanCyclers",
    #         "modelType": "hybrid",
    #         "manufacturingYear": 2022,
    #         "price": 899.99,
    #         "description": "The City Commuter is the perfect bike for navigating busy streets and urban environments. Its lightweight frame, smooth gears, and comfortable riding position make it ideal for daily commuting. Equipped with practical features like fenders, a rear rack, and lights, the City Commuter is ready for any city adventure.",
    #         "image": "https://ebr-prod-bucket.s3.amazonaws.com/r-f-img-webp/review-featured-images/2015-Pedego-City-Commuter-electric-bike-review.webp",
    #         "isNew": False,
    #         "createdAt": datetime.now()
    #     },
    #     {
    #         "name": "Beach Cruiser",
    #         "companyName": "SunsetRides",
    #         "modelType": "cruiser",
    #         "manufacturingYear": 2021,
    #         "price": 699.99,
    #         "description": "Enjoy the breeze and sunshine with the Beach Cruiser. This bike features a comfortable saddle, wide handlebars, and a relaxed riding position, making it perfect for leisurely rides along the coast. Its stylish design and vibrant colors add a touch of fun to every ride, ensuring you always cruise in style.",
    #         "image": "https://www.citygrounds.com/cdn/shop/files/media_a38d76f6-e01c-4441-9ffb-f92b00251f07_grande.png?v=1711393506",
    #         "isNew": True,
    #         "createdAt": datetime.now()
    #     },
    #     {
    #         "name": "Performance Pro",
    #         "companyName": "EliteBikes",
    #         "modelType": "road",
    #         "manufacturingYear": 2023,
    #         "price": 1999.99,
    #         "description": "The Performance Pro is a high-end road bike designed for serious cyclists. Its carbon frame, aerodynamic design, and top-tier components provide exceptional speed, efficiency, and handling. Whether you're competing in races or enjoying long-distance rides, the Performance Pro delivers a superior cycling experience.",
    #         "image": "https://inovtel.pt/cdn/shop/files/00ebb0fabcc50fe608511e81e92c08dd_7dfbad48-9209-4257-aac7-ec4c42c79e76_600x600_crop_center.png?v=1687010214",
    #         "isNew": True,
    #         "createdAt": datetime.now()
    #     },
    #     {
    #         "name": "All-Terrain Adventurer",
    #         "companyName": "MountainKing",
    #         "modelType": "mountain",
    #         "manufacturingYear": 2023,
    #         "price": 1699.99,
    #         "description": "The All-Terrain Adventurer is built for exploring the great outdoors. Its durable frame, advanced suspension, and reliable components make it ideal for tackling a variety of terrains, from rocky trails to muddy paths. With its rugged design and superior performance, the All-Terrain Adventurer is your perfect companion for outdoor escapades.",
    #         "image": "https://www.ezbike.ca/cdn/shop/products/aventure.2-slate-01.jpg?v=1719156584&width=1200",
    #         "isNew": True,
    #         "createdAt": datetime.now()
    #     }
    # ]
    bikes = Bikes.objects.all().order_by('-createdAt')
    bikeForm = BikeForm()
    context = {
        'bikes': bikes,
        'form': bikeForm
    }
    return render(request,'index.html', context)