from django.urls import path
from . import views

urlpatterns = [
    path("", views.tela_inicial, name="index"),
    path("cadastro", views.tela_cadastro, name="cadastro"),
    path("login", views.login_system, name="login"),
    path("fazer_cadastro", views.cadastro, name="fazer_cadastro"),
    path("inicio", views.tela_inicial_logado, name="telaInicio"),
]