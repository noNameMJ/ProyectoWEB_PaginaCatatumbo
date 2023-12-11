from django.http import HttpResponse
from django.template import loader

# Create your views here.
def culturaIndex(request):
    template = loader.get_template("cultura-index.html")
    context = {}
    return HttpResponse(template.render(context,request))