from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path('home/', views.home, name='home'), 
]