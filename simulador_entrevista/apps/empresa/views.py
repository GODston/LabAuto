from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class EmpresaLogin(View):
    
    def get(request):
        return render(request, 'login.html')

