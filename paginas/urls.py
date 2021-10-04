from django.urls import path
from .views import IndexView
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login", views.login_system, name="login"),
    path("cadastro", views.cadastro, name="cadastro"),
    path("inicio", views.tela_inicial_logado, name="telaInicio"),
]