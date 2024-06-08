from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('', views.index),
]