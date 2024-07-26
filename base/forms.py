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
            'image': forms.ClearableFileInput(attrs={'multiple': False, 'class': 'px-3 py-2.5 bg-white rounded w-full', 'placeholder': 'Image URL'}),
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
            'image': forms.ClearableFileInput(attrs={'class': 'px-3 py-2.5 rounded w-full bg-white', 'placeholder': 'Image URL'}),
            'isNew': forms.CheckboxInput(attrs={'class': 'scale-125'}),
        }

class TruckForm(forms.ModelForm):
    class Meta:
        model = Trucks
        fields = ['name', 'companyName', 'modelType', 'manufacturingYear', 'price', 'description', 'image', 'isNew']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Truck name'}),
            'companyName': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Company name'}),
            'modelType': forms.Select(attrs={'class': 'px-3 py-3 rounded w-full'}),
            'manufacturingYear': forms.NumberInput(
                attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Manufacturing year'}),
            'price': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Price'}),
            'description': forms.Textarea(
                attrs={'class': 'px-3 py-3 rounded w-full', 'rows': 8, 'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(
                attrs={
                    'multiple': False,
                    'class': 'px-3 py-2.5 rounded w-full bg-white',
                    'placeholder': 'Image URL'
                }),
            'isNew': forms.CheckboxInput(attrs={'class': 'scale-125'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ['user', 'car', 'rating', 'comment', 'is_approved']

class RatingForm(forms.ModelForm):
    VEHICLE_TYPE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('truck', 'Truck'),
    ]

    vehicle_type = forms.ChoiceField(choices=VEHICLE_TYPE_CHOICES, required=True)
    vehicle_model = forms.ChoiceField(choices=[], required=True)

    class Meta:
        model = Rating
        fields = ['vehicle_type', 'vehicle_model', 'rating', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle_model'].choices = []

    def clean(self):
        cleaned_data = super().clean()
        vehicle_type = cleaned_data.get('vehicle_type')
        vehicle_model = cleaned_data.get('vehicle_model')

        if vehicle_type == 'car':
            vehicle_queryset = Cars.objects.filter(id=vehicle_model)
        elif vehicle_type == 'bike':
            vehicle_queryset = Bikes.objects.filter(id=vehicle_model)
        elif vehicle_type == 'truck':
            vehicle_queryset = Trucks.objects.filter(id=vehicle_model)
        else:
            vehicle_queryset = None

        if not vehicle_queryset:
            raise forms.ValidationError('Invalid vehicle model selected.')

        return cleaned_data