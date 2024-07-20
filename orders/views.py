from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from trucks.models import Trucks
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
