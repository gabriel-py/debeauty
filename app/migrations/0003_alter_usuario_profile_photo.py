# Generated by Django 4.0.1 on 2022-01-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_post_midias_post_midias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='profile_photo',
            field=models.ImageField(default='profile.jpeg', upload_to=''),
        ),
    ]
