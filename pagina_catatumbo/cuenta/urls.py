from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('Cuenta/',views.miCuenta, name='miCuenta'),
]