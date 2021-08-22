from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

def login(request):
    print(request.POST.get('email',None))
    print(request.POST.get('password',None))
    return render(request, 'pos.html', {})

def novo_pedido(request):
    return render(request, 'novo_pedido.html', {})
