from django.contrib import admin
from .models import Bikes
from .models import Rating

# Register your models here.
admin.site.register(Bikes)
admin.site.register(Rating)