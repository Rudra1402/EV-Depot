from django import forms
# from .models import CustomUser
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

#
# class UserRegisterForm(forms.ModelForm):
#     mobile = forms.CharField(max_length=10)
#     gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES)
#
#     class Meta:
#         model = CustomUser
#         fields = ['firstname', 'lastname', 'email', 'password', 'mobile', 'gender']
#         labels = {'firstname': 'First Name', 'lastname': 'Last Name', 'email': 'Email', 'password': 'Password', 'mobile': 'Mobile', 'gender': 'Gender'}
#
#     def save(self, commit=True):
#         user = super(UserRegisterForm, self).save(commit=False)
#         user.password = make_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')




