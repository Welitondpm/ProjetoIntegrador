from django import forms
from django.forms import ModelForm
from .models import Usuario


class CadastroForm(forms.ModelForm):
    login = forms.CharField(
        label="Login:",
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Digite seu login"}),
    )
    senha = forms.CharField(
        label="Senha:",
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Digite sua senha"}),
    )
    # senha_confirm = forms.CharField(label="Confirme sua senha:", max_length=200, widget=forms.Input(attrs={"placeholder": "Confirme sua senha"})))
    nome = forms.CharField(
        label="Nome próprio:",
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Digite seu nome"}),
    )
    email = forms.EmailField(
        label="E-mail:",
        max_length=200,
        widget=forms.EmailInput(attrs={"placeholder": "Ex: exemplo@exemplo.com"}),
    )
    # cpf_cnpj = forms.CharField(label="CPF ou CNPJ:", max_length=200, widget=forms.Input(attrs={"placeholder": "Ex: 123.456.789-10 / 12.345.678/1234-56"})))
    # optestado = (
    #     ("", "Selecione o seu estado"),
    #     ("sc", "Santa Catarina"),
    #     ("rs", "Rio de merda"),
    # )
    # estado = forms.ChoiceField(choices=optestado)
    # optmunicipio = (
    #     ("", "Selecione o seu município"),
    #     ("0", "Araquari"),
    #     ("1", "São Francisco do "),
    # )
    # estado = forms.ChoiceField(choices=optestado)
    # bairro = forms.CharField(label="Bairro:", max_length=200, widget=forms.Input(attrs={"placeholder": "Digite seu bairro"}))
    # rua = forms.CharField(label="Rua:", max_length=200, widget=forms.Input(attrs={"placeholder": "Digite sua rua"}))
    # numero = forms.CharField(label="Número:", max_length=200, widget=forms.Input(attrs={"placeholder": "Digite o número do logradouro"}))
    # complemento = forms.CharField(label="Complemento:", max_length=200, widget=forms.Input(attrs={"placeholder": "Ex: Casa, Apartamento, Condomínio"}))

    class Meta:
        model = Usuario
        fields = ["login", "senha", "nome", "email"]


class LoginForm(forms.Form):
    login = forms.CharField(label="Login:", max_length=200)
    senha = forms.CharField(label="Senha:", max_length=200)