from django.db import models
from django.utils import timezone
from users.models import Buyer

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
    image = models.ImageField(upload_to='bikes/')
    isNew = models.BooleanField(default=True)
    createdAt = models.DateField(default=timezone.now)
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='bikes')

    def __str__(self):
        return self.name