from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def carrito(request):
    return render(request, 'tienda/carrito.html')

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
