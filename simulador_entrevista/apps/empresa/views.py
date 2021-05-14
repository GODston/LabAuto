from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from apps.persona.models import Persona

# Create your views here.
def registro_empresa(request):

    return render(request, "register.html")

def empresas_post(request):

    nombre = request.GET["txtNames"]
    puesto = "PRUEBA"
    edad = 23
    fecha_registro = date.today()
    fecha_Entrevista = date.today()
    personaPrueba = Persona(nombre, edad)

    personaPrueba.save()

    return HttpResponse(nombre)
