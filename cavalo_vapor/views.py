from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def index(request):
    return render(request, "index.html")

#     contexto = {'senha': 0, 'usuario': 0}
#         contexto = {'senha': request.POST['senha'], 'usuario': request.POST['usuario']}
#     return render(request, "login.html", contexto)

def cadastro(request):
    if request.method == 'POST':
        if request.POST['senha'] == request.POST['confirmeSenha']:
            user = User.objects.create_user(request.POST['usuario'], request.POST['email'], request.POST['senha'])
            user.save()
    return render(request, "cadastro.html")

def logar(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['usuario'], password=request.POST["senha"])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, "login.html")

def logout_view(request):
    if User.is_authenticated or User.is_staff:
        logout(request)
        return HttpResponseRedirect('/')

def suporte(request):
    # if request.method == 'POST':
    #     send_mail(
    #         request.POST['motivo'],
    #         request.POST['mensagem'],
    #         'Triunviratoifc@gmail.com',
    #         ['gusferreira1203@gmail.com', 'fel9.renan02@gmail.com', 'welitondpm2003@gmail.com'],
    #         fail_silently=False,
    #     )
    return render(request, "suporte.html")

def fretes(request):
    return render(request, "fretes.html")

def caminhoes(request):
    return render(request, "caminhoes.html")

def perfis(request):
    return render(request, "perfis.html")

def network(request):
    return render(request, "network.html")

def usuario(request):
    return render(request, "usuario.html")

def atividade(request):
    return render(request, "atividade.html")

def chats(request):
    return render(request, "chats.html")
