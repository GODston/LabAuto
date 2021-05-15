from django.shortcuts import render
from django.views.generic import View
from .models import Entrevista

# Create your views here.
class EntrevistaView(View):

    def get(request):
        entrevistas = Entrevista.objects.all()
        data = {
            "empresa": True,
            "listaEntrevistas": entrevistas
        }
        return render(request, 'interviews.html', data)

    def get_detail(request):
        return render(request, 'interview_details.html', {
        "empresa": True
    })
