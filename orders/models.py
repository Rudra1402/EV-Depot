from django.db import models
from django.contrib.auth.models import User

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
