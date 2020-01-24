# Generated by Django 2.2.6 on 2020-01-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloConsulta', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=9)),
                ('telefono', models.CharField(max_length=9)),
                ('consulta', models.TextField(max_length=1000)),
            ],
        ),
    ]
