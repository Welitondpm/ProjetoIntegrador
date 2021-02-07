from django.urls import path
from . import views

app_name = 'cavalo_vapor'
urlpatterns = [
    path("index", views.index, name="index"),
]