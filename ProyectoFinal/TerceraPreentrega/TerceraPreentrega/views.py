from django.template import Template, Context
from django.http import HttpResponse

def saludar(request):
    saludo="HOLA HOLA"
    return HttpResponse(saludo)
