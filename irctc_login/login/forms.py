#with forms.py

from django import forms

# Form for user sign-up
class SignupForm(forms.Form):
    # Username field with a maximum length of 100 characters and marked as required
    username = forms.CharField(max_length=100, required=True)
    
    # Email field, validates for proper email format and is required
    email = forms.EmailField(required=True)
    
    # Phone field with a maximum length of 15 characters, validates as required
    phone = forms.CharField(max_length=15, required=True)
    
    # Department field with predefined choices, marked as required
    department = forms.ChoiceField(
        choices=[
            ('pg-accounting', 'PG Accounting'),
            ('pg-settlement', 'PG Settlement'),
            ('pg-chargeback', 'PG Chargeback'),
            ('tourism', 'Tourism')
        ],
        required=True
    )
    
    # Password field with input hidden for security, marked as required
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    # Confirmation password field with input hidden for security, marked as required
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    # Custom form-wide validation method
    def clean(self):
        """
        Perform validation for form-wide logic, such as checking if
        the password and confirm_password fields match.
        """
        # Retrieve the cleaned data for password and confirm_password
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Validate that both passwords match
        if password and confirm_password and password != confirm_password:
            # Raise an error if passwords do not match
            raise forms.ValidationError("Passwords do not match.")

        # Return the validated data
        return cleaned_data


# Form for user login
class LoginForm(forms.Form):
    # Username field with a maximum length of 100 characters and marked as required
    username = forms.CharField(max_length=100, required=True)
    
    # Password field with input hidden for security, marked as required
    password = forms.CharField(widget=forms.PasswordInput, required=True)

