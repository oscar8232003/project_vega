from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User

        fields=[
            "first_name",
            "username",
            "password1",
            "password2",
        ]

class UpdateUserForm(UserCreationForm):
    class Meta:
        model=User

        fields=[
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

        widgets={
            'username':forms.HiddenInput,
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su apellido'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese su email'}),
        }