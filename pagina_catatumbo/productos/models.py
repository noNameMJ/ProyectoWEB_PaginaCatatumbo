from django.db import models

class TipoProducto(models.Model):
    """
    Modelo que representa los tipos de productos (arte,artesanía,...) los cuales se pueden encontrar productos en la tienda
    """
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    """
    Modelo que representa las cateogrias de los productos que se venden en la tienda
    """
    nombre = models.CharField(max_length=50)
    ref_tipoproducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EstadoProducto(models.Model):
    """
    Modelo que representa los posibles estados configurables para los productos.
    Ejemplo: Agotado, Disponible
    """
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

class Producto(models.Model):
    ref_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    ref_estado = models.ForeignKey(EstadoProducto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    caracteristicas = models.CharField(max_length=400)
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    imagen = models.FileField(upload_to="productos/img_producto")
    def __str__(self):
        return self.nombre