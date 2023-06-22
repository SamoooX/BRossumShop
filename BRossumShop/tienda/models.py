from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, null= False,verbose_name='Apellido')
    correo = models.EmailField(max_length=200, verbose_name='Correo')
    contraseña = models.CharField(max_length=12, null= False, verbose_name='Contraseña')
    contraseña2 = models.CharField(max_length=12, null= False, verbose_name='Contraseña 2')


    def str(self):
            return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=False, verbose_name='Nombre')
    imagen = models.CharField(max_length=500, null=False, verbose_name='Imagen')
    precio = models.IntegerField( null=False, verbose_name='Precio')
    descripcion = models.CharField(max_length=1000, verbose_name='Descripcion')
    stock = models.IntegerField(null=False, verbose_name='Stock')

    def str(self):
        return self.nombre


class DetalleBoleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE, null=False)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=False)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cantidad = models.PositiveIntegerField(null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def str(self):
        return f'Detalle Boleta {self.id}'


class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)
    monto = models.IntegerField(null=False)
    fecha = models.DateField(null=False)

    def str(self):
        return f'Boleta {self.id_boleta}'