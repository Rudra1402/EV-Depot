from django import forms
from .models import CustomUser

class UserRegisterForm(forms.ModelForm):
    mobile = forms.CharField(max_length=10)
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'email', 'password', 'mobile', 'gender']
        labels = {'firstname': 'First Name', 'lastname': 'Last Name', 'email': 'Email', 'password': 'Password', 'mobile': 'Mobile', 'gender': 'Gender'}

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
