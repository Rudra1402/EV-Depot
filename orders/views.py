from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from cars.models import Cars
from trucks.models import Trucks
from bikes.models import Bikes
from .forms import ReviewRatingForm
from .models import CarOrder, BikeOrder, TruckOrder


@login_required
def order_list(request):
    car_orders = CarOrder.objects.filter(user=request.user)
    bike_orders = BikeOrder.objects.filter(user=request.user)
    truck_orders = TruckOrder.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {
        'car_orders': car_orders,
        'bike_orders': bike_orders,
        'truck_orders': truck_orders,
    })


@login_required
def create_truck_order(request, truck_id):
    truck = get_object_or_404(Trucks, id=truck_id)
    TruckOrder.objects.create(truck=truck, user=request.user)
    return redirect('orders:order_list')


def delete_truck_order(request, order_id):
    order = get_object_or_404(TruckOrder, id=order_id, user=request.user)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:order_list')
    return render(request, 'orders/confirm_delete.html', {'order': order})


@login_required
def submit_review_rating(request, vehicle_type, vehicle_id):
    vehicle_model = {'cars': Cars, 'bikes': Bikes, 'trucks': Trucks}.get(vehicle_type)
    if vehicle_model is None:
        return redirect('orders:order_list')  # Redirect to order list if vehicle_type is invalid

    vehicle = get_object_or_404(vehicle_model, id=vehicle_id)
    if request.method == 'POST':
        form = ReviewRatingForm(request.POST)
        if form.is_valid():
            review_rating = form.save(commit=False)
            review_rating.user = request.user
            setattr(review_rating, vehicle_type, vehicle)
            review_rating.save()
            # Print statement for debugging
            print(f"Review saved: {review_rating}")
            return redirect('orders:order_details', vehicle_type=vehicle_type, vehicle_id=vehicle_id)
    else:
        form = ReviewRatingForm()
    return render(request, 'orders/submit_review_rating.html',
                  {'form': form, 'vehicle_type': vehicle_type, 'vehicle': vehicle})

def order_details(request, vehicle_type, vehicle_id):
    vehicle_model = {'cars': Cars, 'bikes': Bikes, 'trucks': Trucks}.get(vehicle_type)
    vehicle = get_object_or_404(vehicle_model, id=vehicle_id)
    review_ratings = vehicle.review_ratings.all()

    # Calculate average rating
    if review_ratings.exists():
        total_rating = sum(r.rating for r in review_ratings)
        avg_rating = total_rating / review_ratings.count()
    else:
        avg_rating = 0

    context = {
        'vehicle': vehicle,
        'vehicle_type': vehicle_type,
        'review_ratings': review_ratings,
        'avg_rating': avg_rating,
    }
    # Print statement for debugging
    print(f"Reviews fetched: {review_ratings}")
    return render(request, 'orders/order_details.html', context)

