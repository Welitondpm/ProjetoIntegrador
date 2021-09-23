from django.contrib import admin
from django.urls import path
from cavalo_vapor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('suporte/', views.suporte, name="suporte"),
    path('fretes/', views.fretes, name="fretes"),
    path('atividade/', views.atividade, name="atividade"),
    path('caminhoes/', views.caminhoes, name="caminhoes"),
    path('chats/', views.chats, name="chats"),
    path('mapa/', views.mapa, name="mapa"),
    path('network/', views.network, name="network"),
    path('perfis/', views.perfis, name="perfis"),
    path('usuario/', views.usuario, name="usuario"),
]
