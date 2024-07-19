from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from trucks.models import Trucks
from .models import Rating, Category
from .forms import CategoryForm, RatingForm
from cars.models import Cars
from bikes.models import Bikes
from .forms import CarsForm, BikesForm, TruckForm

def common_form_view(request, app_name):
    if app_name == 'cars':
        FormClass = CarsForm
        model_class = Cars
        redirect_url = 'cars:homepage'  # Update to your specific redirect URL
    elif app_name == 'bikes':
        FormClass = BikesForm
        model_class = Bikes
        redirect_url = 'bikes:homepage'  # Update to your specific redirect URL
    elif app_name == 'trucks':
        FormClass = TruckForm
        model_class = Trucks
        redirect_url = 'trucks:homepage'  # Update to your specific redirect URL
    else:
        return redirect('error_page')  # Or handle error appropriately
    
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            model_class.objects.create(**data)
            return redirect(reverse(redirect_url))  # Redirect to the appropriate application page
    else:
        form = FormClass()

    return render(request, 'common_form.html', {'form': form, 'app_name': app_name})


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
    categories = Category.objects.all()  # Retrieve all categories
    ratings = Rating.objects.all()  # Retrieve all ratings
    return render(request, 'home.html', {'categories': categories, 'ratings': ratings})


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name = 'category'
