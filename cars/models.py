from django.db import models


# Create your models here.
class Cars(models.Model):
    CAR_TYPES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('hatchback', 'Hatchback'),
        ('wagon', 'Wagon'),
        ('pickup', 'Pickup Truck'),
        ('minivan', 'Minivan'),
        ('crossover', 'Crossover'),
        ('luxury', 'Luxury Car'),
        ('sports', 'Sports Car'),
    ]

    name = models.CharField(max_length=200)
    companyName = models.CharField(max_length=200)
    modelType = models.CharField(max_length=100, choices=CAR_TYPES)
    manufacturingYear = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.URLField()
    isNew = models.BooleanField(default=True)
    createdAt = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "cars"
