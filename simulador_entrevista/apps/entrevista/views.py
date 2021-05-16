from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from datetime import datetime
from .models import Entrevista, Pregunta
from .forms import AgregarEntrevistaForm, EntrevistaForm, AgregarPreguntaForm, PreguntaForm

# Create your views here.
class EntrevistaView(View):

    ## Lista de entrevistas
    def list(request):
        entrevistas = Entrevista.objects.all()
        data = {
            "empresa": True,
            "listaEntrevistas": entrevistas
        }
        return render(request, 'entrevista/listar.html', data)

    ## Agregar entrevista
    def add_entrevista(request):
        data = {
            'empresa': True,
            'formEntrevista': AgregarEntrevistaForm()
        }   
        ## Metodo post    
        if request.method == 'POST':
            formEntrevista = AgregarEntrevistaForm(data=request.POST)
            ## Se guarda la entrevista
            if formEntrevista.is_valid():
                formEntrevista.save()
                return redirect(to="entrevistas")
            else: 
                data["formEntrevista"] = formEntrevista

        return render(request, 'entrevista/agregar.html', data)

    ## Detalle de entrevista y actualizar
    def detail_entrevista(request, id):
        entrevista = Entrevista.objects.get(id=id)
        nuevaPregunta = Pregunta(entrevista=entrevista)
        listaPreguntas = Pregunta.objects.filter(entrevista=id)
    
        ##listaPreguntas = Pregunta.objects.get(entrevista=entrevista.id)
        data = {
            'empresa': True,
            'entrevista': entrevista,
            'formEntrevista': EntrevistaForm(instance=entrevista),
            'formAgregarPregunta': AgregarPreguntaForm(instance=nuevaPregunta),
            'listaPreguntas': listaPreguntas
        }

    
        if request.method == 'POST':
            ## Se actualiza entrevista
            formEntrevista = EntrevistaForm(data=request.POST, instance=entrevista)
            if formEntrevista.is_valid():
                formEntrevista.save()

            ## Se agrega pregunta
            formAgregarPregunta = AgregarPreguntaForm(data=request.POST)
            if formAgregarPregunta.is_valid():
                formAgregarPregunta.save()
            else:
                data["formAgregarPregunta"] = formAgregarPregunta

        return render(request, 'entrevista/modificar.html', data)
    
    ## Eliminar una entrevista
    def delete_entrevista(request, id):
        entrevista = get_object_or_404(Entrevista, id=id)
        entrevista.delete()
        return redirect(to="entrevistas")

class PreguntasView:

    def delete_pregunta(request, id):
        pregunta = get_object_or_404(Pregunta, id=id)
        pregunta.delete()
        return redirect(to="entrevistas")
                