from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .models import Producto,TipoProducto,Categoria

# Vista principal de Productos
def tiendaIndex(request):
    
    #consultar categoria principal y categorias secundarias
    tipoproductos = TipoProducto.objects.all()
    categorias = Categoria.objects.all()

    #Consultar productos
    productos_list = Producto.objects.all()
    #Configurar paginación cada 15 productos
    paginator = Paginator(productos_list, 15)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)
    #Obtener el template
    template = loader.get_template("tienda.html")
    #Agregar el contexto
    context = {"page_obj": page_obj,"tipoproductos":tipoproductos,"categorias":categorias}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def productosCategoria(request):
    # Consultar categoria principal y categorias secundarias
    tipoproductos = TipoProducto.objects.all()

    categoria_principal = request.GET.get('cat_principal')
    categorias = Categoria.objects.filter(ref_tipoproducto__nombre=categoria_principal)
    
    categoria_secundaria = request.GET.get('cat_secundaria', '')
    search_term = request.GET.get('search', '')
    if categoria_secundaria != '' and search_term:
        productos_list = Producto.objects.filter(ref_categoria__nombre=categoria_secundaria, nombre__icontains=search_term)
    elif categoria_secundaria != '':
        productos_list = Producto.objects.filter(ref_categoria__nombre=categoria_secundaria)
    elif search_term != '':
        productos_list = Producto.objects.filter(nombre__icontains=search_term)
    else:
        productos_list = Producto.objects.filter(ref_categoria__ref_tipoproducto__nombre=categoria_principal)


    paginator = Paginator(productos_list, 15)

    # Obtener página
    page_number = request.GET.get('page', 0)
    page_obj = paginator.get_page(page_number)

    # Obtener el template
    template = loader.get_template("tienda-cat-principal.html")

    # Agregar el contexto
    context = {"page_obj": page_obj, "tipoproductos": tipoproductos, "categorias": categorias,"categoria_principal":categoria_principal,"categoria_secundaria":categoria_secundaria}

    # Retornar respuesta http
    return HttpResponse(template.render(context, request))

#Vista para ver detalles de un producto
def detalleProducto(request, id):
    #Consultar producto
    producto = Producto.objects.get(id=id)           

    #Consultar datos de producto
    context = {'producto':producto}
    #Obtener el template
    template = loader.get_template("detalleProducto.html")

    return HttpResponse(template.render(context,request))