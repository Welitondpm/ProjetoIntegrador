from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'cavalo_vapor/index.html')

def dashboard(request):
    return render(request, 'cavalo_vapor/dashboard.html')

def chat(request):
    return render(request, 'cavalo_vapor/chat.html')

def fretes(request):
    return render(request, 'cavalo_vapor/fretes.html')

def perfils(request):
    return render(request, 'cavalo_vapor/perfils.html')

def login(request):
    return render(request, 'cavalo_vapor/login.html')

def cadastro(request):
    return render(request, 'cavalo_vapor/cadastro.html')

def suporte(request):
    return render(request, 'cavalo_vapor/suporte.html')