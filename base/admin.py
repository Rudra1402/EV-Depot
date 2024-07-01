# base/admin.py

from django.contrib import admin
from .models import Category, Rating

admin.site.register(Category)
admin.site.register(Rating)
