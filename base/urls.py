from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ratings/', views.RatingListView.as_view(), name='ratings-list'),
    path('ratings/<int:pk>/', views.RatingDetailView.as_view(), name='ratings-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='categories-detail'),
    path('common_form/<str:app_name>/', views.common_form_view, name='common_form'),
    # other paths as needed
]
