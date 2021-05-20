from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from cavalo_vapor.models import Frete
from cavalo_vapor.form import FretesForm, PerfilForm, UserForm, UserPerfilForm

# Create your views here.


def index(request):
    return render(
        request,
        "cavalo_vapor/index.html",
    )


def cadastro(request):
    superusers = ["fel9.renan02@gmail.com", "gusferreira1203@gmail.com"]
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
    print(formulario)
    return render(request, "cavalo_vapor/cadastro.html", {"form": formulario})


def chat(request):
    return render(request, "cavalo_vapor/chat.html")


def fretes(request):
    fretes = Frete.objects.all()
    contexto = {"fretes": fretes}
    return render(request, "cavalo_vapor/fretes.html", contexto)


def login(request):
    return render(request, "cavalo_vapor/login.html")


def perfis(request):
    users = User.objects.all()
    contexto = {"users": users}
    return render(request, "cavalo_vapor/perfis.html", contexto)


def suporte(request):
    return render(request, "cavalo_vapor/suporte.html")


def logout(request):
    return render(request, "logout.html")


@login_required
def perfil_individual(request):
    if request.method == "POST":
        userUpdate = UserPerfilForm(request.POST, instance=request.user)
        perfilUpdate = PerfilForm(
            request.POST, request.FILES, instance=request.user.usuario
        )
        if userUpdate.is_valid() or perfilUpdate.is_valid():
            userUpdate.save()
            perfilUpdate.save()
            return redirect("perfil_individual")
    else:
        userUpdate = UserPerfilForm(instance=request.user)
        perfilUpdate = PerfilForm(instance=request.user.usuario)

    contexto = {"userUpdate": userUpdate, "perfilUpdate": perfilUpdate}
    return render(request, "cavalo_vapor/perfil_individual.html", contexto)


def chat_individual(request, id_sala):
    return render(request, "cavalo_vapor/chat_individual.html")


def frete_individual(request):
    return render(request, "cavalo_vapor/frete_individual.html")


@login_required
def cadastrar_frete(request):
    if request.method == "POST":
        freteForm = FretesForm(request.POST)
        if freteForm.is_valid():
            freteForm.save()
            return redirect("fretes")
    else:
        freteForm = FretesForm()
    contexto = {"form": freteForm}
    return render(request, "cavalo_vapor/cadastrar_frete.html", contexto)
