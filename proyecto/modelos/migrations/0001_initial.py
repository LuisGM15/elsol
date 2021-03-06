# Generated by Django 3.2.4 on 2021-07-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('clave', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.TextField(verbose_name='Rol')),
                ('descripción', models.TextField(verbose_name='Descripción')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización')),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
    ]
