from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Carrito, Producto, DetalleCarrito,  Boleta, DetalleBoleta
from django.contrib.auth import authenticate, login, logout
from .forms import FormularioUsuario, FormularioLogin
# Create your views here.


def index(request):
    return render(request, 'tienda/index.html')



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
    # Actualizar el atributo total del carrito
    carrito.total = total
    carrito.save()
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
    usuario = request.user
    # Obtener las boletas asociadas al usuario
    boletas = Boleta.objects.filter(id_usuario=usuario)

    boletas_con_detalles = {}  # Diccionario para almacenar las boletas y sus detalles

    total_boletas = {}  # Diccionario para almacenar los totales de cada boleta

    for boleta in boletas:
        # Obtener los detalles de boleta asociados a cada boleta
        detalles = DetalleBoleta.objects.filter(id_boleta=boleta.id_boleta)

        detalles_con_info = []

        total_boleta = 0  # Inicializar el total de la boleta en 0

        for detalle in detalles:
            producto = detalle.id_producto
            imagen = producto.imagen
            nombre = producto.nombre
            valor_unitario = detalle.valor_unitario
            cantidad = detalle.cantidad
            total = detalle.total

            # Crear un diccionario con la información del detalle
            detalle_info = {
                'imagen': imagen,
                'nombre': nombre,
                'valor_unitario': valor_unitario,
                'cantidad': cantidad,
                'total': total
            }

            # Agregar el detalle con la información adicional a la lista
            detalles_con_info.append(detalle_info)


        boletas_con_detalles[boleta] = detalles_con_info  # Agregar los detalles al diccionario de boletas

        total_boletas[boleta] = total_boleta  # Agregar el total de la boleta al diccionario de totales

    # Pasar los diccionarios de boletas y totales a la plantilla en el diccionario de contexto
    context = {
        'boletas': boletas_con_detalles,
        'total_boleta': total_boleta
    }

    return render(request, 'tienda/perfil.html', context)



def inicio_sesion(request):
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password1')
            usuario = authenticate(username=nombre_usuario, password1=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect(to='perfil')
    return render(request, 'registration/login.html',)


def registro(request):
    data = {
        'form':FormularioUsuario()
    }

    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        
    return render(request, 'registration/registro.html', data)

def exit(request):
    logout(request)
    return redirect('/')


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
        boleta = Boleta(id_usuario=request.user,
                        monto=carrito.total, fecha=datetime.now())
        boleta.save()

        # Obtener todos los detalles del carrito asociados al carrito actual
        detalles_carrito = DetalleCarrito.objects.filter(carrito=carrito)

        # Transferir los detalles del carrito a la tabla DetalleBoleta
        for detalle_carrito in detalles_carrito:
            detalle_boleta = DetalleBoleta(id_boleta=boleta, id_producto=detalle_carrito.producto,
                                        valor_unitario=detalle_carrito.producto.precio, cantidad=detalle_carrito.cantidad, total = detalle_carrito.cantidad * detalle_carrito.producto.precio)
            detalle_boleta.save()

        # Eliminar los registros del carrito actual en DetalleCarrito
        detalles_carrito.delete()

        # Redireccionar a una página de confirmación o a otra vista según sea necesario
        return redirect('perfil')
    else:
        # El usuario no está autenticado, redirige a la página de inicio de sesión
        return redirect('login')
    
def mostrar_boleta(request, boleta_id):
    usuario = request.user
    # Obtener la boleta con el ID proporcionado
    boleta = Boleta.objects.get(id_usuario=usuario)

    # Obtener los detalles de boleta asociados a la boleta
    detalles = DetalleBoleta.objects.filter(id_boleta=boleta.id_boleta)

    # Crear una lista para almacenar los detalles con la información adicional
    detalles_con_info = []

    for detalle in detalles:
        producto = detalle.id_producto
        imagen = producto.imagen
        nombre = producto.nombre
        valor_unitario = detalle.valor_unitario
        cantidad = detalle.cantidad
        total = detalle.total

        # Crear un diccionario con la información del detalle
        detalle_info = {
            'imagen': imagen,
            'nombre': nombre,
            'valor_unitario': valor_unitario,
            'cantidad': cantidad,
            'total': total
        }

        # Agregar el detalle con la información adicional a la lista
        detalles_con_info.append(detalle_info)

    # Obtener el total de la boleta
    total_boleta = boleta.monto

    # Pasar los detalles y el total de la boleta a la plantilla en el diccionario de contexto
    context = {
        'detalles': detalles_con_info,
        'total_boleta': total_boleta
    }

    return render(request, 'tienda/detalle_boleta.html', context)
