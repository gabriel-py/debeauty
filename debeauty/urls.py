from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.tela_inicial, name="index"),
    path("cadastro", views.tela_cadastro, name="cadastro"),
    path("login", views.login_system, name="login"),
    path("logout", views.logout_system, name="logout"),
    path("fazer_cadastro", views.cadastro, name="fazer_cadastro"),
    path("inicio", views.tela_inicial_logado, name="telaInicio"),
    path("novo_post", views.cria_novo_post, name="criaNovoPost"),
    path("novo_pedido", views.tela_novo_pedido, name="criaNovoPedido"),
    path("salva_pedido", views.salva_pedido, name="salva_pedido"),
    path("salva_solicitacao", views.salva_solicitacao, name="salva_solicitacao"),
    path("historico", views.tela_historico, name="historico"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)