from django.contrib import admin
from django.urls import path
from cavalo_vapor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
    path('fretes/', views.fretes, name="fretes"),
    path('network/', views.network, name="network"),
    path('caminhoes/', views.caminhoes, name="caminhoes"),
    path('perfis/', views.perfis, name="perfis"),
    path('atividade/', views.atividade, name="atividade"),
    path('usuario/', views.usuario, name="usuario"),
    path('logout_view/', views.logout_view, name="logout"),
    path('suporte/', views.suporte, name="suporte"),
    path('ajax/select_city/', views.select_city, name='select_city'),
    path('ajax/delCaminhoes/', views.delCaminhoes, name='delCaminhoes'),
    path('ajax/delCarreta/', views.delCarreta, name='delCarretas'),
    path('update/updateCaminhao/', views.updateCaminhoes, name='updateCaminhao'),
    path('update/updateCarreta/', views.updateCarreta, name='updateCarreta'),
]
