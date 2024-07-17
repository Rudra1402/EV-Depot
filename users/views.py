from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            CustomUser.objects.create_user(
                email=form.cleaned_data['email'],
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                password=form.cleaned_data['password'],
                mobile=form.cleaned_data['mobile'],
                gender=form.cleaned_data['gender']
            )
            messages.success(request, "Account created successfully!")
            return redirect('users:register')
        else:
            messages.warning(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('bikes:homepage')  # Redirect to some view after login
            else:
                messages.error(request, "Invalid email or password")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})
