from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
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
                messages.success(request, "Se han agregado los datos de la persona correctamente")
            else: 
                data["formPersona"] = formularioPersona

            ## Se guarda el candidato
            if formularioCandidato.is_valid():
                formularioCandidato.save()
                messages.success(request, "Se ha agregado correctamente")
                return redirect(to="candidatos")

            data["formCandidato"] = formularioCandidato

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
                messages.success(request, "Se han actualizado los datos correctamente")
                return redirect(to="detalle_candidato", id=id)
            else:
                data["formPersona"] = formPersona

            if formCandidato.is_valid():
                formCandidato.save()
                messages.success(request, "Se han actualizado los datos correctamente")
                return redirect(to="detalle_candidato", id=id)
            else:
                data["formCandidato"] = formCandidato

        return render(request, 'candidatos/modificar.html', data)

    ## Delete candidato
    def delete(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        candidato.delete()
        messages.success(request, "Se ha eliminado el registro correctamente")
        return redirect(to="candidatos")
    