from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .models import Vacante, Criterio
from .forms import AgregarVacanteForm, VacanteForm, AgregarCriterioForm, CriterioForm

# Create your views here.
class EmpresaLoginView(View):
    
    def get(request):
        return render(request, 'login.html')

class EmpresaRegistroView(View):

    def get(request):
        return render(request, 'register.html')

class EmpresaView(View):

    def get_config(request):

        data = {
            'empresa': True
        }
        return render(request, 'settings.html', data)

class VacantesView(View):

    def get(request):
        listaVacantes = Vacante.objects.all()
        data = {
            'empresa': True,
            'listaVacantes': listaVacantes
        }
        return render(request, 'vacante/listar.html', data)

    ## Agregar vacante
    def add_vacante(request):
        data = {
            'empresa': True,
            'formVacante': AgregarVacanteForm()
        }

        if request.method == 'POST':
            formVacante = AgregarVacanteForm(data=request.POST)
            if formVacante.is_valid():        
                formVacante.save()
                messages.success(request, "Se ha registrado la vacante correctamente")
                return redirect(to="vacantes")
            else:
                data["formVacante"] = formVacante

        return render(request, 'vacante/agregar.html', data)

    ## Modificar vacante
    def detail_vacante(request, id):
        vacante = get_object_or_404(Vacante, id=id)
        formVacante = VacanteForm(instance=vacante)
        data = {
            'empresa': True,
            'vacante': vacante,
            'formVacante': formVacante
        }

        if request.method == 'POST':
            formVacante = VacanteForm(data=request.POST, instance=vacante)
            if formVacante.is_valid():
                formVacante.save()
                messages.success(request, "Se ha guardado la informacion correctamente")
                return redirect(to="detalle_vacante")
            else:
                data["formVacante"] = formVacante

        return render(request, 'vacante/modificar.html', data)
        
    ## Metodo para eliminar una vacante
    def delete_vacante(request, id):
        vacante = get_object_or_404(Vacante, id=id)
        vacante.delete()
        messages.success(request, "Se ha eliminado correctamente")
        return redirect(to="vacantes")

