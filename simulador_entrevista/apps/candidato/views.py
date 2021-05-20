from apps.entrevista.models import Entrevista
from apps.entrevista.models import Pregunta
from apps.empresa.models import Vacante
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from datetime import datetime
from .models import Candidato
from .forms import CandidatoForm, AgregarCandidatoForm, CodigoCandidato
from apps.persona.forms import PersonaForm
from apps.persona.models import Persona
import speech_recognition as sr

# Create your views here.

class CodigoCandidatoView(View):

    ## Vista de buscar codigo
    def search_code(request):
         
        data = {
            "form": CodigoCandidato()
        }

        if request.method == 'POST':
            formCodigo = CodigoCandidato(data=request.POST)
            codigo = request.POST["codigo"]
            candidato = get_object_or_404(Candidato, codigo=codigo)

            if candidato:
                return redirect(to="bienvenida_entrevista", id=candidato.id)
            else:
                messages.error(request, 'Codigo no encontrado')
                data["form"] = formCodigo
                return redirect(to="codigo_candidato")
        
        return render(request, 'codigo_candidato/inicio_candidato.html', data)

    ## Vista de bienvenida para la entrevista
    def welcome_entrevista(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        
        data = {
            "candidatoInfo": candidato
        }

        return render(request, 'codigo_candidato/bienvenida.html', data)

    ## Vista de inicio de la entrevista
    def init_entrevista(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        vac = get_object_or_404(Vacante, vacante = candidato.vacante)
        ent = get_object_or_404(Entrevista, vacante = vac.id)
        preguntas = Pregunta.objects.filter(entrevista = ent.id)
        data = {
            "candidatoInfo": candidato,
            "listaPreguntas": preguntas
        }
        return render(request, 'codigo_candidato/inicio_entrevista.html', data)
    
    ## Vista para guardar la entrevista
    def save_entrevista(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        data = {
            "candidatoInfo": candidato
        }
        return render(request, 'codigo_candidato/guardar_entrevista.html', id)

    def record(request, id, preg):
        r = sr.Recognizer()
        respuesta = "No Funciono"
        with sr.Microphone() as source:
            audio = r.listen(source)
            respuesta = r.recognize_google(audio)

        ## Guardar Respuesta
        candidato = get_object_or_404(Candidato, id=id)
        vac = get_object_or_404(Vacante, vacante = candidato.vacante)
        ent = get_object_or_404(Entrevista, vacante = vac.id)
        preguntas = Pregunta.objects.filter(entrevista = ent.id)
        data = {
            "candidatoInfo": candidato,
            "listaPreguntas": preguntas,
        }
        return render(request, 'codigo_candidato/inicio_entrevista.html', data)

class CandidatoView(View):
    def get(request): 
        candidatos = Candidato.objects.all()
        data = {
            'listaCandidatos': candidatos
        }
        return render(request, 'candidatos/listar.html', data)

    ## Vista para agregar candidatos
    def add_candidato(request):
        data = {
            'formPersona': PersonaForm(),
            'formCandidato': AgregarCandidatoForm()
        }   
        
        if request.method == 'POST':
            formularioCandidato = AgregarCandidatoForm(data=request.POST)
            formularioPersona = PersonaForm(data=request.POST)
            
            ## Se guarda la informacion del candidato
            if formularioPersona.is_valid() and formularioCandidato.is_valid():
                persona = formularioPersona.save()
                formularioCandidato = AgregarCandidatoForm(data=request.POST, instance=Candidato(persona=persona))
                candidato = formularioCandidato.save()
                messages.success(request, "Se ha registrado el candidato correctamente")
                return redirect(to="detalle_candidato", id=candidato.id)
            else: 
                data["formPersona"] = formularioPersona
                data["formCandidato"] = formularioCandidato
            
        return render(request, 'candidatos/agregar.html', data)


    def detail_candidato(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        data = {
            'candidato': candidato,
            'formCandidato': CandidatoForm(instance=candidato),
            'formPersona': PersonaForm(instance=candidato.persona)
        }

        ## Update info candidato
        if request.method == 'POST':
            formPersona = PersonaForm(data=request.POST, instance=candidato.persona)
            formCandidato = CandidatoForm(data=request.POST, instance=candidato)

            if formPersona.is_valid() and formCandidato.is_valid():
                formPersona.save()
                formCandidato.save()
                messages.success(request, "Se han actualizado los datos correctamente")
                return redirect(to="detalle_candidato", id=id)
            else:
                data["formPersona"] = formPersona
                data["formCandidato"] = formCandidato

        return render(request, 'candidatos/modificar.html', data)

    ## Delete candidato
    def delete_candidato(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        candidato.delete()
        messages.success(request, "Se ha eliminado el registro correctamente")
        return redirect(to="candidatos")

    