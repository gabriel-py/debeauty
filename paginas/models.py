from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=220)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)

class Cliente(Usuario):
    ramos_interesse = models.ManyToManyField(Ramo)

class Ramo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)

class Colaborador(Usuario):
    endereco_profissional = models.CharField(max_length=200)
    ramos_atuacao = models.ManyToManyField(Ramo)

class Pedido(models.Model):
    cod_solicitante = models.IntegerField(null=False, blank=False)
    cod_status = models.IntegerField(null=False, blank=False)
    valor_total = models.FloatField(blank=False, null=False)
    faixa_horario = models.CharField(max_length=200)

class Solicitacao(models.Model):
    cod_pedido = models.IntegerField(null=False, blank=False)
    cod_colaborador = models.IntegerField(null=False, blank=False)
    valor = models.FloatField(blank=False, null=False)
    faixa_horario = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    medias = models.ManyToManyField(Media)

class Media(models.Model):
    url = models.CharField(max_length=2000)

class Post(models.Model):
    ramo = models.ManyToManyField(Ramo)
    cod_autor = models.IntegerField(null=False, blank=False)
    conteudo = models.TextField(blank=True, null=True)
    midias = models.ManyToManyField(Media)
    likes = models.ManyToManyField(Likes)

class Likes(models.Model):
    cod_usuario = models.IntegerField(null=False, blank=False)
    
