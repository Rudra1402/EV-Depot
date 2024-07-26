from django import forms
from .models import Trucks

class TruckForm(forms.ModelForm):
    class Meta:
        model = Trucks
        fields = ['name', 'companyName', 'modelType', 'manufacturingYear', 'price', 'description', 'image', 'isNew']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Truck name'}),
            'companyName': forms.TextInput(attrs={'class': 'px-3 py-3 rounded w-full', 'placeholder': 'Company name'}),
            'modelType': forms.Select(attrs={'class': 'px-3 py-3 rounded w-full'}),
            'manufacturingYear': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full','placeholder': 'Manufacturing year'}),
            'price': forms.NumberInput(attrs={'class': 'px-3 py-3 rounded w-full','placeholder': 'Price'}),
            'description': forms.Textarea(attrs={'class': 'px-3 py-3 rounded w-full', 'rows': 8,'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(attrs={
                'multiple': False,
                'class': 'px-3 py-3 rounded w-full',
                'placeholder': 'Image URL'
            }),
            'isNew': forms.CheckboxInput(attrs={'class': 'scale-125'}),
        }
