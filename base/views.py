# base/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Rating, Category
from .forms import CategoryForm, RatingForm


class RatingListView(ListView):
    model = Rating
    template_name = 'ratings/index.html'
    context_object_name = 'ratings'


class RatingDetailView(DetailView):
    model = Rating
    template_name = 'ratings/detail.html'
    context_object_name = 'rating'


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name = 'category'


def home(request):
    # Add any additional context data needed for the home page
    return render(request, 'home.html')
