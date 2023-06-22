from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, null= False,verbose_name='Apellido')
    correo = models.CharField(max_length=200, null= False, verbose_name='Correo')
    contraseña = models.CharField(max_length=12, null= False, verbose_name='Contraseña')
    contraseña2 = models.CharField(max_length=12, null= False, verbose_name='Contraseña 2')


    def str(self):
            return self.nombre