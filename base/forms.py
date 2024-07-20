from django import forms
from .models import Category, Rating
from cars.models import Cars
from bikes.models import Bikes
from trucks.models import Trucks


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['name', 'companyName', 'modelType', 'manufacturingYear', 'price', 'description', 'image', 'isNew']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Car name'}),
            'companyName': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Company name'}),
            'modelType': forms.Select(attrs={'class': 'px-3 py-3 rounded w-full'}),
            'manufacturingYear': forms.NumberInput(
                attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Manufacturing year'}),
            'price': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Price'}),
            'description': forms.Textarea(
                attrs={'class': 'px-3 py-3 rounded w-full', 'rows': 8, 'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(attrs={'multiple': False, 'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Image URL'}),
            'isNew': forms.CheckboxInput(attrs={'class': 'scale-125'}),
        }

class BikesForm(forms.ModelForm):
    class Meta:
        model = Bikes
        fields = ['name', 'companyName', 'modelType', 'manufacturingYear', 'price', 'description', 'image', 'isNew']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Bike name'}),
            'companyName': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Company name'}),
            'modelType': forms.Select(attrs={'class': 'px-3 py-3 rounded w-full'}),
            'manufacturingYear': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full','placeholder': 'Manufacturing year'}),
            'price': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full','placeholder': 'Price'}),
            'description': forms.Textarea(attrs={'class': 'px-3 py-3 rounded w-full', 'rows': 8,'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Image URL'}),
            'isNew': forms.CheckboxInput(attrs={'class': 'scale-125'}),
        }

class TruckForm(forms.ModelForm):
    class Meta:
        model = Trucks
        fields = ['name', 'company_name', 'model_type', 'manufacturing_year', 'price', 'description', 'image', 'is_new']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Truck name'}),
            'company_name': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Company name'}),
            'model_type': forms.Select(attrs={'class': 'px-3 py-3 rounded w-full'}),
            'manufacturing_year': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full','placeholder': 'Manufacturing year'}),
            'price': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full','placeholder': 'Price'}),
            'description': forms.Textarea(attrs={'class': 'px-3 py-3 rounded w-full', 'rows': 8,'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Image URL'}),
            'is_new': forms.CheckboxInput(attrs={'class': 'scale-125'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'car', 'rating', 'comment', 'is_approved']
