from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

def tela_inicial(request, mensagem=None):
    print(mensagem)
    return render(request, "index.html", mensagem)

def tela_cadastro(request):
    return render(request, "index_cadastro.html")

@login_required(login_url='index')
def tela_inicial_logado(request):
    return render(request, "pos.html")

def login_system(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('telaInicio')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    return redirect('index')
    

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        selection = request.POST.get('selection')

        password = make_password(password)

        try:
            aux = User(username=email, password=password)
            aux.save()
            if selection == "cliente":
                user = Cliente(nome=nome, django_user=aux)
                user.save()
            else:
                user = Colaborador(nome=nome, django_user=aux)
                user.save()
        except IntegrityError:
            messages.error(request, "E-mail já se encontra em uso.")
    return redirect('cadastro')