# Generated by Django 3.2.4 on 2021-07-11 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_alter_grupo_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='paterno',
            field=models.TextField(default='Example', verbose_name='Apellido paterno'),
        ),
    ]