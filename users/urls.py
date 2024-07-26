from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name= "users"
urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.UpdateProfile, name='update_profile'),
    path('delete_profile/', views.DeleteProfile, name='delete_profile'),
    path('messages/<int:user_id>', views.user_messages, name="messages"),
]