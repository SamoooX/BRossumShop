from django.contrib import admin
from .models import Usuario
from .models import Producto
from .models import DetalleCarrito
# Register your models here.

class Usuarios(admin.ModelAdmin):
    list_display = ['nombre', 'apellido' , 'correo', 'contraseña', 'contraseña2']
    search_fields = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'stock']
    search_fields = ['nombre', 'precio', 'descripcion', 'stock']
    list_per_page = 10

admin.site.register(Usuario, Usuarios)
admin.site.register(Producto, ProductoAdmin)