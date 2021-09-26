from django.contrib import admin
from django.urls import path
from cavalo_vapor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.logar, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('suporte/', views.suporte, name="suporte"),
    path('fretes/', views.fretes, name="fretes"),
    path('caminhoes/', views.caminhoes, name="caminhoes"),
    path('perfis/', views.perfis, name="perfis"),
    path('network/', views.network, name="network"),
    path('usuario/', views.usuario, name="usuario"),
    path('atividade/', views.atividade, name="atividade"),
    path('logout_view/', views.logout_view, name="logout"),
    path('ajax/select_city/', views.select_city, name='select_city'),
]
