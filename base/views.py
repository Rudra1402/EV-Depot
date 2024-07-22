from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

from trucks.models import Trucks
from .models import Rating, Category
from .forms import CategoryForm, RatingForm
from cars.models import Cars
from bikes.models import Bikes
from .forms import CarsForm, BikesForm, TruckForm

def common_form_view(request, app_name):
    try:
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
            # form = FormClass(request.POST)
            # if form.is_valid():
            #     data = form.cleaned_data
            #     model_class.objects.create(**data)
            return redirect(redirect_url)  # Redirect to the appropriate application page
        else:
            form = FormClass()

        return render(request, 'common_form.html', {'form': form, 'app_name': app_name})
    except Exception as e:
        print(str(e))


class RatingListView(ListView):
    model = Rating
    template_name = 'ratings/index.html'
    context_object_name = 'ratings'

class RatingDetailView(DetailView):
    model = Rating
    template_name = 'ratings/detail.html'
    context_object_name = 'rating'

def rate_item(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            vehicle_type = form.cleaned_data.get('vehicle_type')
            vehicle_model_id = form.cleaned_data.get('vehicle_model')

            if vehicle_type == 'car':
                rating.car_id = vehicle_model_id
            elif vehicle_type == 'bike':
                rating.bike_id = vehicle_model_id
            elif vehicle_type == 'truck':
                rating.truck_id = vehicle_model_id

            rating.save()
            return redirect('home')
    else:
        form = RatingForm()

    return render(request, 'rate_item.html', {'form': form})

def load_vehicle_models(request):
    vehicle_type = request.GET.get('vehicle_type')
    if vehicle_type == 'car':
        models = Cars.objects.all()
    elif vehicle_type == 'bike':
        models = Bikes.objects.all()
    elif vehicle_type == 'truck':
        models = Trucks.objects.all()
    else:
        models = []

    model_choices = [{'id': model.id, 'name': model.name} for model in models]
    return JsonResponse(model_choices, safe=False)

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name = 'category'