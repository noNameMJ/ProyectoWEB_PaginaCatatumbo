from django.http import HttpResponse
from django.template import loader

# Create your views here.
def sobreNosotros(request):
    template = loader.get_template("sobre_nosotros.html")
    context = {}
    return HttpResponse(template.render(context,request))