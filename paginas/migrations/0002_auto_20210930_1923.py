# Generated by Django 3.1.2 on 2021-09-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(max_length=220),
        ),
    ]
