# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import CustomUser

# # Signup Form
# class SignupForm(UserCreationForm):
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=15)
#     department = forms.CharField(max_length=100)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'phone', 'department', 'password1', 'password2']

# # Login Form
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
