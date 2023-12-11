from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

@login_required
def miCuenta(request):
    # Aquí puedes acceder a los detalles del usuario utilizando request.user
    usuario = request.user

    # Puedes pasar cualquier otro dato relacionado con el usuario a la plantilla
    context = {'usuario': usuario}
    template = loader.get_template("mi_cuenta.html")
    return HttpResponse(template.render(context,request))
