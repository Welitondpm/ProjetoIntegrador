from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")