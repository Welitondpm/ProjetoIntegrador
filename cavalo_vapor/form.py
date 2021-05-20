from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Frete, Usuario


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
            "faz_frete",
        ]


class UserPerfilForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class FretesForm(ModelForm):
    class Meta:
        model = Frete
        fields = [
            "descricao",
            "avaliacao_empresa",
            "tipo_de_carga",
            "data_hora_carga",
            "carga",
            "avaliacao_caminhoneiro",
            "valor",
            "tipo_reboque",
            "status_fretes",
            "data_hora_prazo",
            "distancia",
            "data_hora_descarga",
            "descricao_status",
            "peso_inicial",
            "tempo_de_candidato",
        ]
