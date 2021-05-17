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
        fields = [
            "imagem",
            "soma_avaliacoes",
            "foto_capa",
            "logo",
            "qtd_avaliacoes",
            "descricao",
            "modo_preferencia",
        ]


class UserPerfilForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
