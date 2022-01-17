from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Media(models.Model):
    imagem = models.ImageField()

    def __str__(self):
        return "{}".format(self.id)

class Usuario(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, unique=True)
    nome = models.CharField(max_length=220)
    localizacao = models.CharField(max_length=200, null=True)

    foto_perfil = models.ForeignKey(Media, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nome)

class Ramo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    icon = models.ForeignKey(Media, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nome)

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
    ramos_interesse = models.ManyToManyField(Ramo)

    def __str__(self):
        return "{}".format(self.usuario.nome)

class Colaborador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
    endereco_profissional = models.CharField(max_length=200)
    ramos_atuacao = models.ManyToManyField(Ramo)

    def __str__(self):
        return "{}".format(self.usuario.nome)

class Pedido(models.Model):
    cod_status = models.IntegerField(null=False, blank=False)
    valor_total = models.FloatField(blank=False, null=False)
    data_realizacao_desejada = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    solicitante = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.id)

class Solicitacao(models.Model):
    valor = models.FloatField(blank=False, null=False)
    faixa_horario = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)

    media = models.ForeignKey(Media, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.id)

class Post(models.Model):
    conteudo = models.TextField(blank=True, null=True)

    ramo = models.ManyToManyField(Ramo)
    midias = models.ForeignKey(Media, on_delete=models.PROTECT)
    likes = models.ManyToManyField(Usuario)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='person2post')

    def __str__(self):
        return "Post {} de {}".format(self.id, self.autor)
