from django import forms
from .models import Trucks

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
