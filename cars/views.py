from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

from users.models import Buyer
from .utils import upload_image_to_firebase
# Create your views here.
from cars.models import Cars
from .forms import CarForm


# def carindex(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cars:homepage')  # Redirect to the same page to clear the form
#     else:
#         form = CarForm()

#     cars = Cars.objects.all().order_by('-createdAt')
#     car_form = CarForm()
#     context = {
#         'cars': cars,
#         'form': car_form,
#         'visit_counts': request.visit_counts,
#         'most_visited_app': max(request.visit_counts, key=request.visit_counts.get)
#     }
#     return render(request, 'cars/carindex.html', context)

def carindex(request):
    try:
        if request.method == 'POST':
            form = CarForm(request.POST, request.FILES)
            print(request.POST, request.FILES)
            if form.is_valid():
                car = form.save(commit=False)
                
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    image_url = upload_image_to_firebase(image, 'bike_images')
                    car.image = image_url
                    car.user = Buyer.objects.get(pk=4)

                form.save()
                return redirect('cars:homepage')  # Redirect to the same page to clear the form
        else:
            form = CarForm()

        cars = Cars.objects.filter(purchasedBy__isnull=True)

        latest = request.GET.get('latest')
        if latest:
            cars = cars.order_by('-createdAt')

        sort = request.GET.get('sort')
        if sort == 'name':
            cars = cars.order_by('name')

        query = request.GET.get('query')
        if query:
            cars = cars.filter(name__icontains=query)

        carform = CarForm()
        context = {
            'cars': cars,
            'form': carform,
            'visit_counts': request.visit_counts,
            'most_visited_app': max(request.visit_counts, key=request.visit_counts.get)
        }
        return render(request,'cars/carindex.html', context)
    except Exception as e:
        print('this is an error'+str(e))
        return render(request, 'cars/carindex.html', {'error_message': str(e)})



#@login_required
def carById(request, id):
    car = get_object_or_404(Cars, id=id)
    # messages = Message.objects.filter(car=car).order_by('-created_at')

    # if request.method == 'POST':
    #     form = MessageForm(request.POST)
    #     if form.is_valid():
    #         message = form.save(commit=False)
    #         message.car = car
    #         message.user = request.user
    #         message.save()
    #         return redirect('cars:car-by-id', id=id)
    # else:
    #     form = MessageForm()

    # context = {
    #     'car': car,
    #     'messages': messages,
    #     'form': form,
    # }
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
    
def edit_car(request, id):
    car = get_object_or_404(Cars, id=id)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            if 'image' in request.FILES:
                image = request.FILES['image']
                image_url = upload_image_to_firebase(image, 'car_images')
                car.image = image_url
            form.save()
            return redirect('cars:homepage')
    else:
        form = CarForm(instance=car)
        form.fields['image'].initial = None

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'cars/edit_car.html', context)


def car_list(request):
    cars = Cars.objects.all()

    latest = request.GET.get('latest')
    if latest:
        cars = cars.order_by('-createdAt')

    sort = request.GET.get('sort')
    if sort == 'name':
        cars = cars.order_by('name')

    query = request.GET.get('query')
    if query:
        cars = cars.filter(name__icontains=query)
    
    context = {
        'cars': cars
    }
    return render(request, 'cars/carindex.html', context)


# def get_message(request, message_id):
#     message = get_object_or_404(Message, id=message_id)
#     data = {
#         'content': message.content,
#         'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
#         'sender': message.sender.id
#     }
#     return JsonResponse(data)

@login_required
def purchase_car(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    owner = car.user
    return render(request, 'cars/purchase_car.html', {'car': car, 'owner': owner})

@login_required
def complete_purchase(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    buyer = Buyer.objects.get(username=request.user)
    owner = car.user

    # Allocate points
    buyer.points += 100  # or any logic to calculate points
    buyer.save()
    owner.points += 50  # or any logic to calculate points
    owner.save()

    # Mark the bike as purchased
    car.purchasedBy = buyer
    car.save()

    return redirect(reverse('cars:homepage'))