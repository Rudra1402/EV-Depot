# base/admin.py
from django.contrib import admin
from .models import Rating, Category
from cars.models import Cars


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'car', 'rating', 'is_approved']
    list_filter = ['is_approved', 'date_created']
    search_fields = ['user__username', 'car__name', 'rating']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'description']



