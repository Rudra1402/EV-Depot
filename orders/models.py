from django.db import models
from django.contrib.auth.models import User
from cars.models import Cars
from bikes.models import Bikes
from trucks.models import Trucks

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class TruckOrder(Order):
    truck = models.ForeignKey('trucks.Trucks', on_delete=models.CASCADE)

class BikeOrder(Order):
    bike = models.ForeignKey('bikes.Bikes', on_delete=models.CASCADE)

class CarOrder(Order):
    car = models.ForeignKey('cars.Cars', on_delete=models.CASCADE)

class ReviewRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, null=True, blank=True, related_name='review_ratings')
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE, null=True, blank=True, related_name='review_ratings')
    truck = models.ForeignKey(Trucks, on_delete=models.CASCADE, null=True, blank=True, related_name='review_ratings')
    rating = models.PositiveIntegerField()  # 1 to 5 stars
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review on {self.car or self.bike or self.truck}"