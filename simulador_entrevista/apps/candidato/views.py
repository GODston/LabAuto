from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from datetime import datetime
from .models import Candidato
from .forms import CandidatoForm, AgregarCandidatoForm
from apps.persona.forms import PersonaForm
from apps.persona.models import Persona

# Create your views here.

class CodigoCandidatoView(View):

    def get(request):
        return render(request, 'codigo_candidato/index.html')

    def search_code(request):
        codigo = request.GET["txtCode"]
        
        return render(request)

class CandidatoView(View):
    def get(request): 
        candidatos = Candidato.objects.all()
        data = {
            'empresa': True,
            'listaCandidatos': candidatos
        }
        return render(request, 'candidatos/listar.html', data)

    ## Vista para agregar candidatos
    def add_candidato(request):
        data = {
            'empresa': True,
            'formPersona': PersonaForm(),
            'formCandidato': AgregarCandidatoForm()
        }   
        ## Metodo post    
        if request.method == 'POST':
            formularioCandidato = AgregarCandidatoForm(data=request.POST)
            formularioPersona = PersonaForm(data=request.POST)
            
            ## Se guarda la persona
            if formularioPersona.is_valid():
                formularioPersona.save()
                data["mensajePersona"] = "Datos guardados correctamente"
            else: 
                data["form"] = formularioPersona

            ## Se guarda el candidato
            if formularioCandidato.is_valid():
                candidato = Candidato(request.POST)
                candidato.codigo = "RH-" + datetime.now()
                formularioCandidato.save()
                return redirect(to="candidatos")
            else: 
                data["form"] = formularioCandidato

        return render(request, 'candidatos/agregar.html', data)


    def get_detail(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        persona = get_object_or_404(Persona, id=candidato.persona.id)
        data = {
            'empresa': True,
            'candidato': candidato,
            'formCandidato': CandidatoForm(instance=candidato),
            'formPersona': PersonaForm(instance=persona)
        }

        ## Update info candidato
        if request.method == 'POST':
            formPersona = PersonaForm(data=request.POST, instance=persona)
            formCandidato = CandidatoForm(data=request.POST, instance=candidato)

            if formPersona.is_valid():
                formPersona.save()
                data["mensajePersona"] = "Datos guardados correctamente"
            else:
                data["formPersona"] = formPersona

            if formCandidato.is_valid():
                formCandidato.save()
                data["mensajeCandidato"] = "Datos guardados correctamente"
                return redirect(to="candidatos")
            else:
                data["formCandidato"] = formCandidato

        return render(request, 'candidatos/modificar.html', data)

    ## Delete candidato
    def delete(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        candidato.delete()
        return redirect(to="candidatos")
    