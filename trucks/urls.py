from django.contrib import admin
from django.urls import path
from trucks import views

urlpatterns = [
    path('', views.index),
]