from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse



def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        # phone = request.POST.get("phone")
        # department = request.POST.get("department")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        if password != confirm_password:
            return render(request, "signup.html", {"error_message": "Passwords do not match."})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error_message": "Username already exists."})

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error_message": "Email is already registered."})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        # user.first_name = department  # Storing department in the first name field temporarily
        user.save()

        return render(request, "login/signup.html", {"success_message": "Account created successfully. You can now log in."})

    # If GET request
    return render(request, "login/signup.html")



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Successfully Logged In.")
        else:
            return render(request, "login.html", {"error_message": "Invalid username or password"})
    
    # If GET request
    return render(request, "login/login.html")



def home(request):
    return render(request,'login/home.html')