# Generated by Django 3.2.4 on 2021-08-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0020_rename_id_profsor_actividad_id_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrega',
            name='nombre_usuario',
            field=models.TextField(default=1, verbose_name='Autor'),
            preserve_default=False,
        ),
    ]
