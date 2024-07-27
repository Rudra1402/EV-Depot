from django.utils import timezone
from users.models import Buyer
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
    companyName = models.CharField(max_length=200)
    modelType = models.CharField(max_length=100, choices=TRUCK_TYPES)
    manufacturingYear = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='trucks/')
    isNew = models.BooleanField(default=True)
    createdAt = models.DateField(default=timezone.now)
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='trucks')
    purchasedBy = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchased_trucks')

    def __str__(self):
        return self.name

class RatingT(models.Model):
    truck = models.ForeignKey(Trucks, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('truck', 'user')

    def __str__(self):
        return f"{self.truck.name} - {self.user.username} - {self.rating}"

