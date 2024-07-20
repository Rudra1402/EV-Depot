from django.contrib import admin
from django.urls import path
from trucks import views

app_name="trucks"
urlpatterns = [
    path('', views.index, name='homepage'),
    path('<int:id>/', views.truckById, name='truckbyid'),
    path('delete/<int:id>/', views.delete_truck, name='delete_truck'),
]