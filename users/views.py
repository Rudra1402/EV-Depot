from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            custom_user = CustomUser(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],  # Consider hashing passwords
                mobile=form.cleaned_data['mobile'],
                gender=form.cleaned_data['gender']
            )
            custom_user.save()
            messages.success(request, "Account created successfully!")
            return redirect('users:login')
        else:
            messages.warning(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})
