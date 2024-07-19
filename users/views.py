from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Buyer

def Register(request):
    if request.method == 'GET':
        return render(request, "register.html")

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']

        if len(mobile) != 10 or not mobile.isdigit():
            messages.warning(request, "The phone number provided is not 10 digits!")
        elif mobile.startswith('0'):
            messages.warning(request, "The phone number provided is not valid!")
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                Buyer.objects.create(username=user, firstname=firstname, email=email, mobile=mobile, address=address, city=city)
                messages.success(request, "Account created successfully!")
                return redirect('base:home')
            except IntegrityError:
                messages.warning(request, "Account already exists!")
                return redirect('users:register')
        return render(request, "register.html")


def LoginUser(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("from login", user)
            print("current: ", timezone.now())

            # Set session variable
            request.session['last_login'] = str(timezone.now())

            messages.success(request, "Logged in successfully!")
            return redirect('base:home')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('users:login')

    return render(request, "login.html")


