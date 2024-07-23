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
<<<<<<< HEAD
    createdAt = models.DateField(auto_now_add=True)

=======
    createdAt = models.DateField(default=timezone.now)
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='cars')
    purchasedBy = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchased_cars')
    
>>>>>>> 1cc19404698a0f8a9272e8c7568772b6e7e1d0f9
    class Meta:
        verbose_name_plural = "cars"

    def __str__(self):
        return self.name
