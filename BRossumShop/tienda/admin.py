from django.contrib import admin
from .models import Usuario
from .models import Producto
# Register your models here.

class Usuarios(admin.ModelAdmin):
    list_display = ['nombre', 'apellido' , 'correo', 'contraseña', 'contraseña2']
    search_fields = ['nombre']


admin.site.register(Usuario, Usuarios)

admin.site.register(Producto)