from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class CodigoCandidato(View):

    def get(request):
        return render(request, 'index.html')

    def search_code(request):
        codigo = request.GET["txtCode"]
        
        return render(request)