from django.urls import path
from . import views

app_name = 'cavalo_vapor'
urlpatterns = [
    path("index", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("chat", views.chat, name="chat"),
    path("fretes", views.fretes, name="fretes"),
    path("perfils", views.perfils, name="perfils"),
    path("login", views.login, name="login"),
    path("cadastro", views.cadastro, name="cadastro"),
    path("suporte", views.suporte, name="suporte"),
]