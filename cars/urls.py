from django.contrib import admin
from django.urls import path
from cars import views

app_name = 'cars'
urlpatterns = [
    path('', views.carindex, name='homepage'),
    path('<int:id>/', views.carById, name='car-by-id'),
    path('delete/<int:id>/', views.deleteCar, name='delete-car'),
    path('edit/<int:id>/', views.edit_car, name='edit-bike'),
    # path('messages/<int:message_id>/', views.get_message, name='get-message'),
]
