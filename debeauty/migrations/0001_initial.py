# Generated by Django 4.0.1 on 2022-01-23 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_profissional', models.CharField(max_length=200, null=True)),
                ('localizacao', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_status', models.IntegerField()),
                ('valor_total', models.FloatField()),
                ('data_realizacao_desejada', models.DateField()),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='debeauty.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(default='profile.jpeg', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(null=True)),
                ('faixa_horario', models.CharField(max_length=200, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='debeauty.colaborador')),
                ('media', models.ManyToManyField(to='debeauty.Media')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='debeauty.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField(blank=True, null=True)),
                ('likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('midias', models.ManyToManyField(to='debeauty.Media')),
                ('ramo', models.ManyToManyField(to='debeauty.Ramo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person2post', to='debeauty.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='colaborador_pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.BooleanField(null=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debeauty.colaborador')),
                ('solicitacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debeauty.solicitacao')),
            ],
        ),
        migrations.AddField(
            model_name='colaborador',
            name='ramos_atuacao',
            field=models.ManyToManyField(to='debeauty.Ramo'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='debeauty.usuario'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ramos_interesse',
            field=models.ManyToManyField(to='debeauty.Ramo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='debeauty.usuario'),
        ),
    ]
