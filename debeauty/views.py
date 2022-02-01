from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import BaseCreateView

from .models import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse

def tela_inicial(request, mensagem=None):
    if(request.user.is_authenticated):
        return redirect('telaInicio')
    return render(request, "index.html", mensagem)

def tela_cadastro(request):
    return render(request, "index_cadastro.html")

@login_required(login_url='index')
def tela_inicial_logado(request):
    Posts = Post.objects.all()
    usuario_logado = Usuario.objects.filter(user=request.user)[0]
    if Posts is not None:
        Posts = reversed(Posts)
    context = {'posts': Posts, 'usuario': usuario_logado}

    if request.user.groups.filter(name__in=['cliente']):
        return render(request, "pos.html", context)
    else:
        return render(request, "pos_colaborador.html", context)

def login_system(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('telaInicio')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    return redirect('index')

@login_required(login_url='index')    
def logout_system(request):
    logout(request)
    return redirect('index')

def cadastro(request):
    if request.method == "POST":
        selection = request.POST.get('selection')

        nome = request.POST.get('name')
        sobrenome = request.POST.get('last_name')
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')

        password = make_password(password)

        try:
            new_user = User(username=user, email=email, password=password)
            new_user.first_name = nome
            new_user.last_name = sobrenome
            new_user.save()

            usuario = Usuario.objects.create(user=new_user)

            if selection == "cliente":
                group = Group.objects.get(name='cliente')
                new_user.groups.add(group)
                Cliente.objects.create(usuario=usuario, user=new_user)
            else:
                group = Group.objects.get(name='colaborador')
                new_user.groups.add(group)
                Colaborador.objects.create(usuario=usuario, user=new_user)

        except IntegrityError:
            new_user.delete()
            messages.error(request, "Usuário já se encontra em uso.")

    return redirect('cadastro')

@login_required(login_url='index')
def cria_novo_post(request):
    if request.method == "POST":
        usuario = Usuario.objects.filter(user=request.user)
        conteudo = request.POST.get('conteudo')
        post = Post.objects.create(conteudo=conteudo, usuario=usuario[0])
        post.save()
    return redirect('telaInicio')

@login_required(login_url='index')
def tela_novo_pedido(request):
    ramos = Ramo.objects.all()
    context = {'ramos': ramos}
    return render(request, "novo_pedido.html", context)

@login_required(login_url='index')
def salva_pedido(request):
    print(request.GET["data"])
    cliente = Cliente.objects.filter(user=request.user)[0]
    pedido = Pedido.objects.create(data_realizacao_desejada=request.GET["data"], solicitante=cliente, cod_status=0)
    mensagem = "Seu pedido foi salvo e a ele foi atribuido o código " + str(pedido.id) + ". Quando desejar, adicione solicitações a ele clicando abaixo."
    return JsonResponse({"response":mensagem}, safe=False)

@login_required(login_url='index')
def salva_solicitacao(request):
    ramo = Ramo.objects.filter(id=request.GET["id_ramo"])
    descricao = request.GET["descricao"]
    media = request.GET["media"]
    media = Media.objects.create(url=media)
    pedido = Pedido.objects.filter(id=request.GET["pedido"])
    Solicitacao.objects.create(ramo=ramo, descricao=descricao, media=media, pedido=pedido)
    mensagem = "Sua solicitação foi cadastrada com sucesso. Aguarde pela resposta de um de nossos colaboradores!"
    return JsonResponse({"response":mensagem}, safe=False)