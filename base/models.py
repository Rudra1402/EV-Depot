# base/models.py
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from cars.models import Cars
from bikes.models import Bikes
from trucks.models import Trucks


# base/models.py

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


#
# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     car = models.ForeignKey(Cars, on_delete=models.CASCADE)  # ForeignKey to Cars model
#     rating = models.DecimalField(max_digits=3, decimal_places=2)  # Allow for decimal ratings
#     comment = models.TextField()
#     date_created = models.DateTimeField(default=timezone.now)
#     is_approved = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.user.username} - {self.car.companyName} {self.car.name} Rating"
#
#     class Meta:
#         ordering = ['-date_created']  # Order ratings by date created descending

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, null=True, blank=True, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bikes, null=True, blank=True, on_delete=models.CASCADE)
    truck = models.ForeignKey(Trucks, null=True, blank=True, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user} - {self.rating}'

    class Meta:
        ordering = ['-date_created']
