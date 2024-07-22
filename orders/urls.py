# orders/urls.py
from django.urls import path
from .views import order_list, create_truck_order, delete_truck_order, submit_review_rating, order_details

app_name = 'orders'

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create-truck-order/<int:truck_id>/', create_truck_order, name='create_truck_order'),
    path('delete_truck_order/<int:order_id>/', delete_truck_order, name='delete_truck_order'),
    path('<str:vehicle_type>/<int:vehicle_id>/', order_details, name='order_details'),
    path('<str:vehicle_type>/<int:vehicle_id>/submit_review_rating/', submit_review_rating,
         name='submit_review_rating'),

]
