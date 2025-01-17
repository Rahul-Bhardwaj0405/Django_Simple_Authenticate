#through html files

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


#through python forms

#from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
#from .forms import SignupForm, LoginForm
#from django.http import HttpResponse

# View to handle user signup
#def signup_view(request):
    #if request.method == 'POST':  # Handle form submission
        #form = SignupForm(request.POST)  # Bind form data from the request
        #if form.is_valid():  # Validate the form
            # Extract validated form data
            #username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            #phone = form.cleaned_data['phone']
            #department = form.cleaned_data['department']
            #password = form.cleaned_data['password']

            # Check if the username already exists in the database
            #if User.objects.filter(username=username).exists():
                # Render the signup page with an error message if the username exists
                #return render(request, 'login/signup.html', {'form': form, 'error_message': 'Username already exists.'})

            # Check if the email is already registered
            #if User.objects.filter(email=email).exists():
                # Render the signup page with an error message if the email exists
                #return render(request, 'login/signup.html', {'form': form, 'error_message': 'Email is already registered.'})

            # Save the new user to the database
            #user = User.objects.create_user(username=username, email=email, password=password)
            # Temporarily store additional user details in the first_name and last_name fields
            #user.first_name = phone  # Storing phone in first_name
            #user.last_name = department  # Storing department in last_name
            #user.save()  # Save the user instance to the database

            # Render the signup page with a success message
            #return render(request, 'login/signup.html', {'form': form, 'success_message': 'Signup successful!'})
        #else:
            # If the form is invalid, re-render the signup page with error messages
            #return render(request, 'login/signup.html', {'form': form, 'error_message': 'Please correct the errors below.'})
    #else:
        # If the request method is GET, render an empty form
        #form = SignupForm()
    #return render(request, 'login/signup.html', {'form': form})


# View to handle user login
#def login_view(request):
    #if request.method == 'POST':  # Handle form submission
        #form = LoginForm(request.POST)  # Bind form data from the request
        #if form.is_valid():  # Validate the form
            # Extract validated login data
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']

            # Authenticate the user with provided credentials
            #user = authenticate(request, username=username, password=password)
            #if user is not None:  # If authentication is successful
                #login(request, user)  # Log the user in
                #return HttpResponse("Successfully Logged In.")  # Respond with a success message
            #else:
                # Render the login page with an error message if authentication fails
                #return render(request, 'login/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
        #else:
            # If the form is invalid, re-render the login page with error messages
            #return render(request, 'login/login.html', {'form': form, 'error_message': 'Invalid login details.'})
    #else:
        # If the request method is GET, render an empty form
        #form = LoginForm()
    #return render(request, 'login/login.html', {'form': form})


# View to handle the home page rendering
#def home(request):
    # Render the home.html template
    #return render(request, 'home.html')
