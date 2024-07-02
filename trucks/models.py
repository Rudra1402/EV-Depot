from django.db import models

class Trucks(models.Model):
    TRUCK_TYPES = [
        ('pickup', 'Pickup Truck'),
        ('semi', 'Semi-Truck'),
        ('box', 'Box Truck'),
        ('dump', 'Dump Truck'),
        ('flatbed', 'Flatbed Truck'),
        ('tanker', 'Tanker Truck'),
    ]

    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    model_type = models.CharField(max_length=100, choices=TRUCK_TYPES)
    manufacturing_year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.URLField()
    is_new = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "trucks"
