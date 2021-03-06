from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from cavalo_vapor.form import UserForm, PerfilForm, UserPerfilForm
from django.contrib import messages
from .form import *
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def index(request):
    return render(request, "cavalo_vapor/index.html",)


# def cadastro(request):
#     superusers = ['fel9.renan02@gmail.com', 'gusferreira1203@gmail.com']
#     if request.method == "POST":
#         formulario = UserForm(request.POST)
#         if formulario.is_valid():
#             if formulario.cleaned_data.get("email") in superusers:
#                 User.objects.create_user(
#                     username=formulario.cleaned_data.get("username"),
#                     email=formulario.cleaned_data.get("email"),
#                     password=formulario.cleaned_data.get("password1"),
#                     is_staff=True,
#                     is_superuser=True,
#                 )
#             else:
#                 formulario.save()
#                 username = formulario.cleaned_data.get("username")

#                 # email = formulario.cleaned_data.get("email")
#                 messages.success(
#                     request,
#                     f"Conta registrada com sucesso {username}! Faça o login e aproveite!",
#                 )
#                 return redirect("login")
#     else:
#         formulario = UserForm()
#     return render(request, "cavalo_vapor/cadastro.html", {"form": formulario})


def cadastro(request):
    superusers = ['fel9.renan02@gmail.com', 'gusferreira1203@gmail.com']
    if not request.method == "POST":
        formulario = UserForm()
    formulario = UserForm(request.POST)
    if not formulario.is_valid():
        return render(request, "cavalo_vapor/cadastro.html", {"form": formulario})
    if not formulario.cleaned_data.get("email") in superusers:
        formulario.save()
        username = formulario.cleaned_data.get("username")

        # email = formulario.cleaned_data.get("email")
        messages.success(
            request,
            f"Conta registrada com sucesso {username}! Faça o login e aproveite!",
        )
        return redirect("login")
    User.objects.create_user(
        username=formulario.cleaned_data.get("username"),
        email=formulario.cleaned_data.get("email"),
        password=formulario.cleaned_data.get("password1"),
        is_staff=True,
        is_superuser=True,
    )
    return render(request, "cavalo_vapor/cadastro.html", {"form": formulario})


def chat(request):
    return render(request, "cavalo_vapor/chat.html")


def frete_individual(request, id_frete):
    return render(request, "cavalo_vapor/frete_individual.html")


def fretes(request):
    return render(request, "cavalo_vapor/fretes.html")


def login(request):
    return render(request, "cavalo_vapor/login.html")


def perfis(request):
    return render(request, "cavalo_vapor/perfis.html")


def suporte(request):
    return render(request, "cavalo_vapor/suporte.html")


def logout(request):
    return render(request, "logout.html")


@login_required
def perfil_individual(request):
    usuario = request.user
    formUser = UserPerfilForm(instance=usuario)
    formProfile = PerfilForm(instance=usuario)
    if request == request.POST:
        if request.method == "POST":
            formProfile = PerfilForm(
                request.POST, request.FILES, instance=usuario)
            formUser = UserPerfilForm(request.POST)
            if formUser.is_valid():
                formUser.save()
            if formProfile.is_valid():
                formProfile.save()
    contexto = {'form1': formProfile, 'form2': formUser}
    return render(request, "cavalo_vapor/perfil_individual.html", contexto)


def chat_individual(request, id_sala):
    return render(request, "cavalo_vapor/chat_individual.html")
