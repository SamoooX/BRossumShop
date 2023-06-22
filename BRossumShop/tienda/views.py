from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Carrito, Producto, DetalleCarrito
# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def carrito(request):
    # Obtener el carrito del usuario actual
    usuario = request.user  # Suponiendo que estás utilizando autenticación de Django
    carrito = Carrito.objects.get(usuario=usuario)

    # Obtener los detalles del carrito
    detalles = carrito.detallecarrito_set.all()

    # Pasar los detalles a la plantilla en el diccionario de contexto
    context = {
        'detalles': detalles
    }

    return render(request, 'tienda/carrito.html', context)


def producto(request):
    return render(request, 'tienda/producto.html')

def acercade(request):
    return render(request, 'tienda/acercade.html')

def perfil(request):
    return render(request, 'tienda/perfil.html')

def inicio_sesion(request):
    return render(request, 'tienda/Inicio_Sesion.html')

def registro(request):
    return render(request, 'tienda/Registro.html')

def agregar_carrito(request, id):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        usuario = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    else:
        carrito, created = Carrito.objects.get_or_create(usuario=None)

    # Obtener el producto correspondiente al ID
    producto = get_object_or_404(Producto, id=id)

    # Crear un nuevo detalle de carrito
    detalle_carrito = DetalleCarrito(carrito=carrito, producto=producto, valor_unitario=producto.precio, cantidad=1, total=producto.precio)
    detalle_carrito.save()

    # Guardar los cambios en el carrito y el detalle del carrito
    carrito.save()

    # Redireccionar a la página del carrito o a donde desees
    return redirect(to='producto')  # Reemplaza 'carrito' con el nombre de tu URL para la página del carrito