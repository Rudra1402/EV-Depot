from django.contrib import admin
from django.urls import path
from bikes import views

app_name="bikes"
urlpatterns = [
    path('', views.index, name='homepage'),
    path('<int:id>/', views.bikeById, name='bikebyid'),
    path('edit/<int:id>/', views.edit_bike, name='edit_bike'),
    path('delete/<int:id>/', views.delete_bike, name='delete_bike'),
    path('purchase/<int:bike_id>/', views.purchase_bike, name='purchase_bike'),
    path('complete_purchase/<int:bike_id>/', views.complete_purchase, name='complete_purchase'),
    path('rate/<int:bike_id>/', views.rate_bike, name='rate_bike'),
]