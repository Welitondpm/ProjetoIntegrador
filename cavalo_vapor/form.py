from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields, widgets
from .models import *


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PerfilForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude = ['usuario']


class UserPerfilForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']
