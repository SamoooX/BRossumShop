from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Carrito, Producto, DetalleCarrito,  Boleta, DetalleBoleta
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
    product = Producto.objects.all()
    context = {"product":product}
    return render(request,'tienda/producto.html', context)


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

def eliminar_dcarrito(request, id):
    detalleC = DetalleCarrito.objects.get(id=id)
    detalleC.delete()

    return redirect(to="carrito")

def finalizar_compra(request):
    # Obtener el carrito actual del usuario (puedes usar el ID del usuario)
    carrito = Carrito.objects.get(usuario=request.user)

    # Crear una nueva instancia de Boleta con los datos necesarios
    boleta = Boleta(usuario=request.user, monto=carrito.total, fecha=datetime.now())
    boleta.save()

    # Obtener todos los detalles del carrito asociados al carrito actual
    detalles_carrito = DetalleCarrito.objects.filter(carrito=carrito)

    # Transferir los detalles del carrito a la tabla DetalleBoleta
    for detalle_carrito in detalles_carrito:
        detalle_boleta = DetalleBoleta(boleta=boleta, producto=detalle_carrito.producto, valor_unitario=detalle_carrito.producto.precio, cantidad=detalle_carrito.cantidad, total=detalle_carrito.total)
        detalle_boleta.save()

    # Eliminar los registros del carrito actual en DetalleCarrito
    detalles_carrito.delete()

    # Redireccionar a una página de confirmación o a otra vista según sea necesario
    return redirect('confirmacion_compra')