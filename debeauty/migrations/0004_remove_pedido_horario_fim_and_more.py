# Generated by Django 4.0.1 on 2022-01-27 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debeauty', '0003_remove_ramo_descricao_alter_ramo_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='horario_fim',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='horario_inicio',
        ),
    ]