# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, firstname, lastname, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, firstname=firstname, lastname=lastname, **extra_fields)
#         user.set_password(password)  # This hashes the password
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, firstname, lastname, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(email, firstname, lastname, password, **extra_fields)
#
# class CustomUser(AbstractBaseUser):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )
#
#     email = models.EmailField(unique=True)
#     firstname = models.CharField(max_length=30)
#     lastname = models.CharField(max_length=30)
#     mobile = models.CharField(max_length=10)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['firstname', 'lastname']
#
#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class Buyer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, max_length=80, unique=True, blank=True)
    firstname = models.CharField(max_length=80, blank=True)
    lastname = models.CharField(max_length=80, blank=True)  # Added lastname field
    email = models.EmailField(max_length=80, unique=True)
    mobile = models.CharField(max_length=11, null=False)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    points = models.PositiveIntegerField(default =0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.email}"

    def _str_(self):
        return str(self.firstname)
