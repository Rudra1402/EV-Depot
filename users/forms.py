from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    mobile = forms.CharField(max_length=10)
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'mobile', 'gender']
        labels = {'email': 'Email', 'first_name': 'First Name', 'last_name': 'Last Name', 'password': 'Password', 'mobile': 'Mobile', 'gender': 'Gender'}
