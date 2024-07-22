from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name= "users"
urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
]