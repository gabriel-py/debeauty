from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    imagem = models.ImageField()

    def __str__(self):
        return "{}".format(self.id)

class Usuario(models.Model):
    profile_photo = models.ImageField(default='profile.jpeg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return "{}".format(self.user.username)

class Ramo(models.Model):
    nome = models.CharField(max_length=200, null=True)
    icon = models.ImageField(null=True)

    def __str__(self):
        return "{}".format(self.nome)

class Cliente(models.Model):
    localizacao = models.CharField(max_length=200, null=True)

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    ramos_interesse = models.ManyToManyField(Ramo)

    def __str__(self):
        return "{}".format(self.user)

class Colaborador(models.Model):
    endereco_profissional = models.CharField(max_length=200, null=True)
    localizacao = models.CharField(max_length=200, null=True)

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    ramos_atuacao = models.ManyToManyField(Ramo)

    def __str__(self):
        return "{}".format(self.user.name)

class Pedido(models.Model):
    cod_status = models.IntegerField(blank=False, null=False)
    valor = models.FloatField(null=True)
    data_realizacao_desejada = models.DateField()

    solicitante = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return "{}".format(self.id)

class Solicitacao(models.Model):
    ramo = models.ForeignKey(Ramo, on_delete=models.PROTECT, null=True)
    descricao = models.CharField(max_length=200, null=True)
    media = models.ImageField(null=True)
    data_pedido = models.DateField()

    valor = models.FloatField(blank=False, null=True)
    horario_inicio = models.TimeField(null=True)
    horario_fim = models.TimeField(null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT, null=True)
    cod_status = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "{}".format(self.id)

class Post(models.Model):
    conteudo = models.TextField(blank=True, null=True)

    ramo = models.ManyToManyField(Ramo)
    midias = models.ManyToManyField(Media)
    likes = models.ManyToManyField(User)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='person2post')

    def __str__(self):
        return "Post {} de {}".format(self.id, self.usuario.user.username)

class colaborador_pedido(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    resposta = models.BooleanField(null=True)

    def __str__(self):
        return "Colaborador {} deu para o pedido {} a resposta".format(self.colaborador, self.solicitacao, self.resposta)
