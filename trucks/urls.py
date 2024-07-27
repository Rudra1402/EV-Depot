from django.contrib import admin
from django.urls import path
from trucks import views

app_name="trucks"
urlpatterns = [
    path('', views.index, name='homepage'),
    path('<int:id>/', views.truckById, name='truckbyid'),
    path('edit/<int:id>/', views.edit_truck, name='edit_truck'),
    path('delete/<int:id>/', views.delete_truck, name='delete_truck'),
    path('purchase/<int:truck_id>/', views.purchase_truck, name='purchase_truck'),
    path('complete_purchase/<int:truck_id>/', views.complete_purchase, name='complete_purchase'),
    path('rate/<int:truck_id>/', views.rate_truck, name='rate_truck'),
]