from django.db import models
from django.urls import reverse
# Create your models here.


class Tipo(models.Model):

    tipoDeConsulta = models.CharField(max_length=200)

    def __str__(self):
        return self.tipoDeConsulta

class Consulta(models.Model):

    tituloConsulta = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    rut = models.CharField(max_length=9)
    telefono = models.CharField(max_length=9)
    consulta = models.TextField(max_length=1000)
    tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.tituloConsulta} ({self.nombre})'