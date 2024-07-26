from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Buyer
from bikes.models import Bikes
from cars.models import Cars
from trucks.models import Trucks
from .forms import UserLoginForm

def Register(request):
    if request.method == 'GET':
        return render(request, "register.html")

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']

        # Validate input fields
        errors = []
        if len(username) < 5:
            errors.append("Username must be at least 5 characters long!")
        if len(firstname) < 5:
            errors.append("Firstname must be at least 5 characters long!")
        if len(lastname) < 5:
            errors.append("Lastname must be at least 5 characters long!")
        if len(password) < 5:
            errors.append("Password must be at least 5 characters long!")
        if len(address) < 5:
            errors.append("Address must be at least 5 characters long!")
        if len(city) < 5:
            errors.append("City must be at least 5 characters long!")
        if not mobile.isdigit():
            errors.append("Mobile number should only contain digits!")
        if len(mobile) != 10:
            errors.append("The phone number provided is not 10 digits!")
        if mobile.startswith('0'):
            errors.append("The phone number provided is not valid!")

        if errors:
            for error in errors:
                messages.warning(request, error)
            return render(request, "register.html")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            Buyer.objects.create(username=user, firstname=firstname, lastname=lastname, email=email, mobile=mobile, address=address, city=city)
            messages.success(request, "Account created successfully!")
            return redirect('users:login')
        except IntegrityError:
            messages.warning(request, "Account already exists!")
            return redirect('users:register')

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

            request.session['last_login'] = datetime.now().isoformat()
            request.session['user_id'] = user.id
            last_login = request.session.get('last_login')
            request.session['user_name'] = user.username

            response = redirect('base:home')
            response.set_cookie('user_id', user.id, max_age=3600)

            messages.success(request, "Logged in successfully!")
            return redirect('base:home')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")

def LogoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('users:login')

@login_required
def profile(request):
    user = request.user
    visit_counts = request.visit_counts
    most_visited_app = max(visit_counts, key=visit_counts.get)

    # Fetch the Buyer instance
    try:
        buyer = Buyer.objects.get(username=user)
        points = buyer.points
        bikes = Bikes.objects.filter(purchasedBy=buyer)
        cars = Cars.objects.filter(purchasedBy=buyer)
        trucks = Trucks.objects.filter(purchasedBy=buyer)
    except Buyer.DoesNotExist:
        points = 0  # Default value if the Buyer instance is not found
        bikes = None
        cars = None
        trucks = None

    # points = user.points
    if points < 100:
        badge = 'bronze_badge.png'
    elif points < 150:
        badge = 'silver_badge.png'
    else:
        badge = 'gold_badge.png'

    context = {
        'visit_counts': visit_counts,
        'most_visited_app': most_visited_app,
        'badge': badge,
        'bikes': bikes,
        'cars': cars,
        'trucks': trucks
    }
    return render(request, 'profile.html', context)

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        user = request.user
        buyer = get_object_or_404(Buyer, username=user)

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']

        # Validate input fields
        if len(firstname) < 5 or len(lastname) < 5 or len(address) < 5 or len(city) < 5:
            messages.warning(request, "Firstname or Lastname or Address or and City must be at least 5 characters long!")
        elif not mobile.isdigit():
            messages.warning(request, "Mobile number should only contain digits!")
        elif len(mobile) != 10:
            messages.warning(request, "The phone number provided is not 10 digits!")
        elif mobile.startswith('0'):
            messages.warning(request, "The phone number provided is not valid!")
        else:
            buyer.firstname = firstname
            buyer.lastname = lastname
            buyer.mobile = mobile
            buyer.address = address
            buyer.city = city
            buyer.save()

            messages.success(request, "Profile updated successfully!")
            return redirect('users:profile')

    else:
        return render(request, 'update_profile.html')

@login_required
def DeleteProfile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Profile deleted successfully!")
        return redirect('users:register')

@login_required
def user_messages(request, user_id):
    seller = Buyer.objects.get(pk=user_id)
    if seller is None:
        return HttpResponse("<h2>Seller not found!</h2>")
    context = {
        'range': range(4)
    }
    return render(request, "messages.html", context)