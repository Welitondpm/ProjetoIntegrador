from django.urls import path
from . import views

app_name = "cavalo_vapor"
urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro", views.cadastro, name="cadastro"),
    path("chat/<int:id_sala>", views.chat_individual, name="chat_individual"),
    path("chat", views.chat, name="chat"),
    path("frete/<int:id_frete>", views.frete_individual, name="frete_individual"),
    path("fretes", views.fretes, name="fretes"),
    path("login", views.login, name="login"),
    path("perfil/<int:id_perfil>", views.perfil_individual, name="perfil_individual"),
    path("perfis", views.perfis, name="perfis"),
    path("suporte", views.suporte, name="suporte"),
]
