from django.db import models

# Create your models here.
class Bikes(models.Model):
    BIKE_TYPES = [
        ('road', 'Road Bike'),
        ('mountain', 'Mountain Bike'),
        ('hybrid', 'Hybrid Bike'),
        ('cruiser', 'Cruiser Bike')
    ]

    name = models.CharField(max_length=200)
    companyName = models.CharField(max_length=200)
    modelType = models.CharField(max_length=100, choices=BIKE_TYPES)
    manufacturingYear = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.URLField()
    isNew = models.BooleanField(default=True)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name