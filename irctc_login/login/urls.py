# when data through html forms
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path('home/', views.home, name='home'), 
]

#when data through python forms
#from django.urls import path
#from . import views  # Importing views from the current application

# URL patterns for the application
#urlpatterns = [
    # Route for the signup page
    #path('signup/', views.signup_view, name='signup'),  
    # Maps the URL `/signup/` to the `signup_view` function in `views.py`
    # The `name='signup'` allows this route to be referred to by the name 'signup' in templates or reverse functions.

    # Route for the login page
    #path('login/', views.login_view, name='login'),  
    # Maps the URL `/login/` to the `login_view` function in `views.py`
    # The `name='login'` allows this route to be referred to by the name 'login' in templates or reverse functions.
#]
