from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class EmpresaLogin(View):
    
    def get(request):
        return render(request, 'login.html')

class EmpresaRegistro(View):

    def get(request):
        return render(request, 'register.html')

class Empresa(View):

    def get_config(request):
        return render(request, 'settings.html', {
            "empresa": True
        })

