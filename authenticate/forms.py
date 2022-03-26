from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from django import forms
from django.forms import ModelForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']


