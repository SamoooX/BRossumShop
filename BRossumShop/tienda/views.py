from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from .models import Carrito, Producto, DetalleCarrito,  Boleta, DetalleBoleta
from .forms import FormularioUsuario
# Create your views here.


def index(request):
    return render(request, 'tienda/index.html')

@login_required
def carrito(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        usuario = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    else:
        carrito, created = Carrito.objects.get_or_create(usuario=None)

    # Obtener los detalles del carrito
    detalles = carrito.detallecarrito_set.all()
    total = sum(detalle.producto.precio for detalle in detalles)
    # Pasar los detalles a la plantilla en el diccionario de contexto
    context = {
        'detalles': detalles,
        'total': total
    }

    return render(request, 'tienda/carrito.html', context)


def producto(request):
    product = Producto.objects.all()
    context = {"product": product}
    return render(request, 'tienda/producto.html', context)


def acercade(request):
    return render(request, 'tienda/acercade.html')

@login_required
def perfil(request):
    return render(request, 'tienda/perfil.html')


def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
    return render(request, 'tienda/Inicio_Sesion.html')


def registro(request):
    data = {
        'form':FormularioUsuario()
    }

    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Te has registrado correctamente"
    return render(request, 'registration/Registro.html', data)

def exit(request):
    logout(request)
    return redirect('tienda/index.html')


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
    detalle_carrito = DetalleCarrito(
        carrito=carrito, producto=producto, cantidad=1)
    detalle_carrito.save()

    # Guardar los cambios en el carrito y el detalle del carrito
    carrito.save()

    # Redireccionar a la página del carrito o a donde desees
    # Reemplaza 'carrito' con el nombre de tu URL para la página del carrito
    return redirect(to='producto')


def eliminar_dcarrito(request, id):
    detalleC = DetalleCarrito.objects.get(id=id)
    detalleC.delete()
    return redirect(to="carrito")


def finalizar_compra(request):
    if request.user.is_authenticated:
            # El usuario está autenticado, procede con la finalización de la compra
            # ...
        # Obtener el carrito actual del usuario (puedes usar el ID del usuario)
        carrito = Carrito.objects.get(usuario=request.user)

        # Crear una nueva instancia de Boleta con los datos necesarios
        boleta = Boleta(usuario=request.user,
                        monto=carrito.total, fecha=datetime.now())
        boleta.save()

        # Obtener todos los detalles del carrito asociados al carrito actual
        detalles_carrito = DetalleCarrito.objects.filter(carrito=carrito)

        # Transferir los detalles del carrito a la tabla DetalleBoleta
        for detalle_carrito in detalles_carrito:
            detalle_boleta = DetalleBoleta(boleta=boleta, producto=detalle_carrito.producto,
                                        valor_unitario=detalle_carrito.producto.precio, cantidad=detalle_carrito.cantidad, total=detalle_carrito.total)
            detalle_boleta.save()

        # Eliminar los registros del carrito actual en DetalleCarrito
        detalles_carrito.delete()

        # Redireccionar a una página de confirmación o a otra vista según sea necesario
        return redirect('confirmacion_compra')
    else:
        # El usuario no está autenticado, redirige a la página de inicio de sesión
        return redirect('Inicio_Sesion/')
