from django.db import models
from django.contrib.auth.models import User
from cars.models import Cars

# Create your models here.



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.car} - {self.rating}'
