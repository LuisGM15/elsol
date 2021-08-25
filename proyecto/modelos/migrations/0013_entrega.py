# Generated by Django 3.2.4 on 2021-08-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0012_duda_contenido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_actividad', models.TextField()),
                ('id_usuario', models.TextField()),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
                'ordering': ['-create_at'],
            },
        ),
    ]
