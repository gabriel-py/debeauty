from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Media(models.Model):
    url = models.CharField(max_length=2000)

class Usuario(models.Model):
    nome = models.CharField(max_length=220)
    cpf = models.CharField(max_length=11)
    localizacao = models.CharField(max_length=200, null=True)
    tipo_usuario = models.CharField(max_length=200, null=True)

    foto_perfil = models.ForeignKey(Media, on_delete=models.PROTECT, null=True)
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome)

class Ramo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    icon_url = models.CharField(max_length=200)

class Cliente(Usuario):
    ramos_interesse = models.ManyToManyField(Ramo)

class Colaborador(Usuario):
    endereco_profissional = models.CharField(max_length=200)
    ramos_atuacao = models.ManyToManyField(Ramo)

class Pedido(models.Model):
    cod_status = models.IntegerField(null=False, blank=False)
    valor_total = models.FloatField(blank=False, null=False)
    faixa_horario = models.CharField(max_length=200)

    solicitante = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Solicitacao(models.Model):
    valor = models.FloatField(blank=False, null=False)
    faixa_horario = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)

    medias = models.ManyToManyField(Media)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

class Post(models.Model):
    conteudo = models.TextField(blank=True, null=True)

    ramo = models.ManyToManyField(Ramo)
    midias = models.ManyToManyField(Media)
    likes = models.ManyToManyField(User)
    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    
