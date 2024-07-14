from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CustomUser
from django.db import IntegrityError

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']

        if len(mobile) != 10 or not mobile.isdigit():
            messages.warning(request, "The phone number provided is not 10 digits!")
        elif mobile.startswith('0'):
            messages.warning(request, "The phone number provided is not valid!")
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                custom_user = CustomUser.objects.create(
                    user=user,
                    firstname=firstname,
                    mobile=mobile,
                    gender=gender,
                    address=address,
                    city=city,
                    state=state
                )
                messages.success(request, "Account created successfully!")
                return redirect('users:login')
            except IntegrityError:
                messages.warning(request, "Account already exists!")
                return redirect('users:register')

        return render(request, 'register.html')
