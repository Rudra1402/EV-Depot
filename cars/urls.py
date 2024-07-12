from django.contrib import admin
from django.urls import path
from cars import views

app_name = 'cars'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('<int:id>/', views.carById, name='car-by-id'),
    path('delete/<int:id>/', views.deleteCar, name='delete-car'),
]
