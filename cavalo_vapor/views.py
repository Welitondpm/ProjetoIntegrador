from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .form import *
from .models import *
from .login import loginVerify

# Create your views here.


def index(request):
    listaObj = Usuario.objects.all()
    listaObj2 = Email.objects.all()
    contexto = {"objetos": listaObj, "objetos2": listaObj2}
    return render(request, "cavalo_vapor/index.html", contexto)


def cadastro(request):
    userform = CadastroForm()
    if request.method == "POST":
        userform = CadastroForm(request.POST)
        if userform.is_valid():
            Usuario.objects.create(**userform.cleaned_data)
            print(request.POST)
        else:
            # print(userform.errors)
            print(userform.errors)
    contexto = {"user": userform}
    return render(request, "cavalo_vapor/cadastro.html", contexto)


#
# def cadastro(request):
#     emailform = EmailForm()
#     if request.method == "POST":
#         emailform = EmailForm(request.POST)
#         if emailform.is_valid():
#             Email.objects.create(**emailform.cleaned_data)
#             print(request.POST)
#         else:
#             # print(userform.errors)
#             print(emailform.errors)
#     contexto = {"user": emailform}
#     return render(request, "cavalo_vapor/cadastro.html", contexto)


# def cadastro(request):
#     userform = CadastroForm()
#     emailform = EmailForm()
#     if request.method == "POST":
#         userform = CadastroForm(request.POST)
#         emailform = EmailForm(request.POST)
#         if userform.is_valid():
#             Usuario.objects.create(**userform.cleaned_data)
#         else:
#             print(userform.errors)
#             print(emailform.errors)
#     contexto = {"user": userform, "email": emailform}
#     return render(request, "cavalo_vapor/cadastro.html", contexto)


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
    loginform = LoginForm()
    if request.method == "POST":
        perfil = request.POST["login"]
        password = request.POST["senha"]
        loginVerify(perfil, password)
    contexto = {"loginform": loginform}
    return render(request, "cavalo_vapor/login.html", contexto)


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
