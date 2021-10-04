from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

class IndexView(TemplateView):
    template_name = "index.html"

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
            return redirect('index')
    return redirect('index')
    

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('name')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        selection = request.POST.get('selection')

        password = make_password(password)

        aux = User(username=email, password=password)
        aux.save()
        user = Usuario(nome=nome, cpf=cpf, tipo_usuario=selection, django_user=aux)
        user.save()
    return redirect('index')

def tela_inicial_logado(request):
    return render(request, "pos.html")
