# Generated by Django 3.2.4 on 2021-08-21 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0010_actividad_duda_respuesta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duda',
            options={'ordering': ['-create_at'], 'verbose_name': 'Duda', 'verbose_name_plural': 'Dudas'},
        ),
        migrations.AlterModelOptions(
            name='respuesta',
            options={'ordering': ['-create_at'], 'verbose_name': 'Respuesta', 'verbose_name_plural': 'Respuestas'},
        ),
    ]