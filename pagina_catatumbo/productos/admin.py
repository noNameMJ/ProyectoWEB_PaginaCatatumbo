from django.contrib import admin
from .models import TipoProducto, Categoria, EstadoProducto, Producto


admin.site.register(TipoProducto)
admin.site.register(Categoria)
admin.site.register(EstadoProducto)
admin.site.register(Producto)