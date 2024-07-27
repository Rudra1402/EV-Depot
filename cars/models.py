from django.db import models
from users.models import Buyer
from django.utils import timezone
from django.conf import settings

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
    image = models.ImageField(upload_to='bikes/')
    isNew = models.BooleanField(default=True)
    createdAt = models.DateField(default=timezone.now)
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='cars')
    purchasedBy = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchased_cars')
    
    class Meta:
        verbose_name_plural = "cars"

    def __str__(self):
        return self.name

class RatingC(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('car', 'user')

    def __str__(self):
        return f"{self.car.name} - {self.user.username} - {self.rating}"


class Car:
    pass

# class Message(models.Model):
#     car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='messages')
#     sender = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['created_at']

#     def __str__(self):
#         return f"{self.sender.username} to {self.recipient.username}: {self.content[:50]}"

