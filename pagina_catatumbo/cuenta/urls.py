from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('Cuenta/',views.miCuenta, name='miCuenta'),
    path('Carrito/',views.carritoCompras, name='carritoCompras'),
    path('Pedidos/',views.pedidos, name='pedidos'),
    path('Agregar/<id>',views.agregarProducto, name='agregarProducto'),
    path('Borrar/<id>',views.borrarProductoCarrito, name='borrarProducto'),
]