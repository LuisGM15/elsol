# Generated by Django 3.2.4 on 2021-08-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0014_respuesta_id_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='ID_duda',
            field=models.TextField(verbose_name='Id Duda'),
        ),
    ]
