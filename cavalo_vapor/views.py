from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")

def suporte(request):
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
