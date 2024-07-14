from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(forms.ModelForm):
    mobile = forms.CharField(max_length=10)
    # gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'email', 'password', 'mobile']
        labels = {'firstname': 'First Name', 'lastname': 'Last Name', 'email': 'Email', 'password': 'Password', 'mobile': 'Mobile'}
