# Generated by Django 4.0.1 on 2022-01-27 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debeauty', '0004_remove_pedido_horario_fim_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='valor_total',
        ),
    ]