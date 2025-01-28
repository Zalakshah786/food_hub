

# Importing necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Register new user
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to homepage after registration
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

# User Login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect("home")  # Redirect to homepage after logout
