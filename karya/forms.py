from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username    = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleUsername', 'placeholder': 'Username'}))
    first_name  = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleFirstName', 'placeholder': 'First Name'}))
    last_name   = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleLastName', 'placeholder': 'Last Name'}))
    email       = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'placeholder': 'Email Address'}))
    password1   = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputPassword', 'placeholder': 'Password'}))
    password2   = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleRepeatPassword', 'placeholder': 'Password Confirmation'}))

    password1.help_text = ''
    password2.help_text = ''

    class Meta:
        model = User
        fields = ("username", "first_name", "email", 'last_name')
