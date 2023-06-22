from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, null= False,verbose_name='Apellido')
    correo = models.EmailField(max_length=200, verbose_name='Correo')
    contraseña = models.CharField(max_length=12, null= False, verbose_name='Contraseña')
    contraseña2 = models.CharField(max_length=12, null= False, verbose_name='Contraseña 2')


    def __str__(self):
            return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=False, verbose_name='Nombre')
    imagen = models.CharField(max_length=500, null=False, verbose_name='Imagen')
    precio = models.DecimalField( null=False, max_digits=10, decimal_places=2, verbose_name='Precio' )
    descripcion = models.CharField(max_length=1000, default='Descripción predeterminada', verbose_name='Descripcion')
    stock = models.IntegerField(null=False, verbose_name='Stock')

    def __str__(self):
        return self.nombre


class DetalleBoleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE, null=False)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=False)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cantidad = models.PositiveIntegerField(null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return f'Detalle Boleta {self.id}'


class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=False)
    monto = models.IntegerField(null=False)
    fecha = models.DateField(null=False)

    def __str__(self):
        return f'Boleta {self.id_boleta}'

class Carrito(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, blank=True)
    productos = models.ManyToManyField('Producto', through='DetalleCarrito')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.usuario:
            return f'Carrito del usuario: {self.usuario.nombre}'
        else:
            return 'Carrito de invitado'

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Detalle del carrito: {self.carrito.id} - Producto: {self.producto.nombre}'
