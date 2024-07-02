from django.urls import path
from . import views

urlpatterns = [
    path('ratings/', views.RatingListView.as_view(), name='ratings-list'),
    path('ratings/<int:pk>/', views.RatingDetailView.as_view(), name='ratings-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='categories-detail'),
    # other paths as needed
]
