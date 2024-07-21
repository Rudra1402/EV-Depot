from django.urls import path
from . import views


app_name= "users"
urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
]