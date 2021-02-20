from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .form import CadastroForm
from .models import *

# Create your views here.


def index(request):
    listaObj = Usuario.objects.all()
    contexto = {"objetos": listaObj}
    return render(request, "cavalo_vapor/index.html", contexto)


def cadastro(request):
    form = CadastroForm()
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            Usuario.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    contexto = {"formulario": form}
    return render(request, "cavalo_vapor/cadastro.html", contexto)


# def cadastro(request):
# valorInicial = {"login": "", "senha": "", "nome": "", "email": ""}
# form = CadastroFormInputs(request.POST or None)
# contexto = {"formulario": form}
# return render(request, "cavalo_vapor/cadastro.html", contexto)


def chat_individual(request, id_sala):
    return render(request, "cavalo_vapor/chat_individual.html")


def chat(request):
    return render(request, "cavalo_vapor/chat.html")


def frete_individual(request, id_frete):
    return render(request, "cavalo_vapor/frete_individual.html")


def fretes(request):
    return render(request, "cavalo_vapor/fretes.html")


def login(request):
    return render(request, "cavalo_vapor/login.html")


def perfil_individual(request, id_perfil):
    return render(request, "cavalo_vapor/perfil_individual.html")


# só to testando (como sempre), para voltar como era antes, eu apago
info = {
    "nome": "Renan",
    "ação": "fazendo merda",
    "resultado": "weliton falando, que merda tu ta fazendo",
}


def perfis(request):
    return render(request, "cavalo_vapor/perfis.html", info)


def suporte(request):
    return render(request, "cavalo_vapor/suporte.html")
