from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .models import Vacante, Criterio
from .forms import AgregarVacanteForm, VacanteForm, AgregarCriterioForm

# Create your views here.
class EmpresaView(View):

    def login(request):
        return render(request, 'empresa/login.html')

    def register(request):
        return render(request, 'empresa/register.html')

    def settings(request):
        data = {
            'empresa': True
        }
        return render(request, 'settings.html', data)


class VacanteView(View):

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
        nuevoCriterio = Criterio(vacante=vacante)
        formVacante = VacanteForm(instance=vacante)
        listaCriterios = Criterio.objects.filter(vacante=id)

        data = {
            'empresa': True,
            'vacante': vacante,
            'formVacante': formVacante,
            'formAgregarCriterio': AgregarCriterioForm(instance=nuevoCriterio),
            'listaCriterios': listaCriterios,
        }

        if request.method == 'POST':
            formVacante = VacanteForm(data=request.POST, instance=vacante)
            if formVacante.is_valid():
                formVacante.save()
                messages.success(request, "Se ha guardado la informacion correctamente")
                return redirect(to="detalle_vacante", id=id)
            else:
                data["formVacante"] = formVacante
            
            formAgregarCriterio = AgregarCriterioForm(data=request.POST)
            if formAgregarCriterio.is_valid():
                formAgregarCriterio.save()
                messages.success(request, "Se ha guardado la informacion correctamente")
                return redirect(to="detalle_vacante", id=id)
            else:
                data["formAgregarCriterio"] = formAgregarCriterio

        return render(request, 'vacante/modificar.html', data)
        
    ## Metodo para eliminar una vacante
    def delete_vacante(request, id):
        vacante = get_object_or_404(Vacante, id=id)
        vacante.delete()
        messages.success(request, "Se ha eliminado correctamente")
        return redirect(to="vacantes")

class CriterioView(View):

    def delete_criterio(request, vacante_id, criterio_id):
        criterio = get_object_or_404(Criterio, id=criterio_id)
        criterio.delete()
        messages.success(request, "Se ha eliminado el criterio correctamente")
        return redirect(to="detalle_vacante", id=vacante_id)

