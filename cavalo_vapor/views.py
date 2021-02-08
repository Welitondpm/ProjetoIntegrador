from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'cavalo_vapor/index.html')

def teste(request):
    return render(request, 'cavalo_vapor/teste.html')