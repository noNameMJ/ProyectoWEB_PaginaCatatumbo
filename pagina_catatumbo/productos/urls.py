from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.tiendaIndex, name='tiendaIndex'),
    path('tienda',views.productosCategoria, name='productosCategoria'),
    path('detalle/<id>/',views.detalleProducto, name='detalleProducto'),
]