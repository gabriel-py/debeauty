from django.urls import path
from .views import IndexView
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="inicio"),
    path("pos", views.login, name="login"),
    path("novo_pedido", views.novo_pedido, name="novo_pedido"),
]