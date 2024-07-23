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

from cars.models import Cars
from bikes.models import Bikes
from trucks.models import Trucks
from .forms import UserLoginForm

# Created Register function to collect data like username,firstname and email which helps to register as user.
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

# Created login function to check user login and password to redirect home or give errors if password incorrect.
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


@login_required
def profile(request):
    user = request.user
    visit_counts = request.visit_counts
    most_visited_app = max(visit_counts, key=visit_counts.get)

    # Fetch the Buyer instance
    try:
        buyer = Buyer.objects.get(username=user)
        points = buyer.points
        purchased_cars = Cars.objects.filter(purchasedBy=buyer)
        purchased_bikes = Bikes.objects.filter(purchasedBy=buyer)
        #purchased_trucks = Trucks.objects.filter(purchasedBy=buyer)

        # Check if any vehicles were purchased
        has_purchased_cars = purchased_cars.exists()
        has_purchased_bikes = purchased_bikes.exists()
        #has_purchased_trucks = purchased_trucks.exists()
    except Buyer.DoesNotExist:
        points = 0  # Default value if the Buyer instance is not found

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
        'purchased_cars': purchased_cars,
        'purchased_bikes': purchased_bikes,
        #'purchased_trucks': purchased_trucks,
        'has_purchased_cars': has_purchased_cars,
        'has_purchased_bikes': has_purchased_bikes,
        #'has_purchased_trucks': has_purchased_trucks,
    }
    return render(request, 'profile.html', context)

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        user = request.user
        buyer = get_object_or_404(Buyer, username=user)

        buyer.firstname = request.POST['firstname']
        buyer.lastname = request.POST['lastname']
        buyer.mobile = request.POST['mobile']
        buyer.address = request.POST['address']
        buyer.city = request.POST['city']
        buyer.save()

        # messages.success(request, "Profile updated successfully!")
        return redirect('users:profile')
    else:
        return render(request, 'update_profile.html')

@login_required
def DeleteProfile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        # messages.success(request, "Profile deleted successfully!")
        return redirect('users:register')

@login_required
def messages(request, user_id):
    seller = Buyer.objects.get(pk=user_id)
    if seller is None:
        return HttpResponse("<h2>Seller not found!</h2>")
    context = {
        'range': range(4)
    }
    return render(request, "messages.html", context)
