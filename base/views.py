from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Rating, Category


class RatingListView(ListView):
    model = Rating
    template_name = 'ratings/index.html'
    context_object_name = 'ratings'


class RatingDetailView(DetailView):
    model = Rating
    template_name = 'ratings/detail.html'
    context_object_name = 'rating'


# base/views.py


def home(request):
    return render(request, 'home.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name = 'category'
