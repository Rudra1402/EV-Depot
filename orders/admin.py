from django.contrib import admin
from .models import CarOrder, BikeOrder, TruckOrder

@admin.register(CarOrder)
class CarOrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'user', 'ordered_at')
    search_fields = ('car__name', 'user__username')

@admin.register(BikeOrder)
class BikeOrderAdmin(admin.ModelAdmin):
    list_display = ('bike', 'user', 'ordered_at')
    search_fields = ('bike__name', 'user__username')

@admin.register(TruckOrder)
class TruckOrderAdmin(admin.ModelAdmin):
    list_display = ('truck', 'user', 'ordered_at')
    search_fields = ('truck__name', 'user__username')
