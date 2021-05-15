from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Candidato

# Create your views here.

class CodigoCandidatoView(View):

    def get(request):
        return render(request, 'index.html')

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
        return render(request, 'candidates.html', data)

    def get_detail(request, id):
        candidato = Candidato.objects.get(id=id)
        data = {
            'empresa': True,
            'candidato': candidato
        }
        return render(request, 'candidate_details.html', data)

    def update_detail(request, id):
        candidato = get_object_or_404(Candidato, id=id)
        return JsonResponse({'code': 200})

    ##TODO: Revisar la creacion de formularios