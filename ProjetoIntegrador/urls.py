"""ProjetoIntegrador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from cavalo_vapor import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("chat/<int:id_sala>", views.chat_individual, name="chat_individual"),
    path("chat", views.chat, name="chat"),
    path("frete/<int:id>", views.frete_individual, name="frete_individual"),
    path("fretes", views.fretes, name="fretes"),
    path("login/", auth_views.LoginView.as_view(template_name="cavalo_vapor/login.html"), name="login",),
    path("perfil/", views.perfil_individual, name="perfil_individual"),
    path("perfis", views.perfis, name="perfis"),
    path("suporte", views.suporte, name="suporte"),
    path("logout/", auth_views.LogoutView.as_view(
        template_name="cavalo_vapor/logout.html"), name="logout",),
]
