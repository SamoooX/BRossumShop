from django.contrib import admin
from .models import Producto
from .models import DetalleCarrito, Carrito
from .models import Boleta
from .models import DetalleBoleta

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'stock']
    search_fields = ['nombre', 'precio', 'descripcion', 'stock']
    list_per_page = 10

admin.site.register(Producto, ProductoAdmin)
admin.site.register(DetalleCarrito)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
admin.site.register(Carrito)