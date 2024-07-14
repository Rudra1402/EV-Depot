from django import forms
from .models import Category, Rating


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'car', 'rating', 'comment', 'is_approved']
