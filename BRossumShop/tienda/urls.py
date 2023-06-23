from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('carrito/', views.carrito, name="carrito"),
    path('producto/', views.producto, name="producto"),
    path('acercade/', views.acercade, name="acercade"),
    path('login/', views.inicio_sesion, name="login"),
    path('perfil/', views.perfil, name="perfil"),
    path('Registro/', views.registro, name="registro"),
    path('agregar_carrito/<id>/', views.agregar_carrito, name='agregar_carrito'),
    path('eliminar_dcarrito/<id>/', views.eliminar_dcarrito, name='eliminar_dcarrito'),
    path('finalizar_compra', views.finalizar_compra, name='finalizar_compra'),
    path('logout/', views.exit, name='exit'),
    
]
