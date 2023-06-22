from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=12)