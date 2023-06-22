from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('carrito/', views.carrito, name="carrito"),
    path('producto/', views.producto, name="producto"),
    path('acercade/', views.acercade, name="acercade"),
    path('Inicio_Sesion/', views.inicio_sesion, name="Inicio_Sesion"),
    path('perfil/', views.perfil, name="perfil"),
    path('Registro/', views.registro, name="registro"),
]
