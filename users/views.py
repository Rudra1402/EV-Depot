from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegisterForm
from .models import CustomUser
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            CustomUser.objects.create(

                firstname=form.cleaned_data['first_name'],
                mobile=form.cleaned_data['mobile'],
                gender=form.cleaned_data['gender'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state']
            )
            messages.success(request, "Account created successfully!")
            return redirect('users:login')
        else:
            messages.warning(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})
