# Generated by Django 3.2.4 on 2021-08-24 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0016_alter_respuesta_id_duda'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='nombre_usuario',
            field=models.TextField(default='nombre', verbose_name='Autor'),
            preserve_default=False,
        ),
    ]
