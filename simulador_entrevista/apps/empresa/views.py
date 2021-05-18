from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .models import Vacante, Criterio, Empresa
from .forms import AgregarEmpresaForm, AgregarVacanteForm, VacanteForm, AgregarCriterioForm, CustomUserCreationForm
from apps.persona.forms import PersonaForm
from django.contrib.auth import authenticate, login

# Create your views here.
class EmpresaView(View):

    def register(request):

        data = {
            'form': CustomUserCreationForm(),
            'formPersona': PersonaForm(),
            'formAgregarEmpresa': AgregarEmpresaForm(),
        }

        if request.method == 'POST':
            formUsuario = CustomUserCreationForm(data=request.POST)
            formPersona = PersonaForm(data=request.POST)
            formAgregarEmpresa = AgregarEmpresaForm(data=request.POST)
            if formUsuario.is_valid() and formPersona.is_valid() and formAgregarEmpresa.is_valid():
                user = formUsuario.save()
                persona = formPersona.save()
                empresa = Empresa(persona=persona, usuario=user)
                formAgregarEmpresa = AgregarEmpresaForm(data=request.POST, instance=empresa)
                formAgregarEmpresa.save()
                user = authenticate(username=formUsuario.cleaned_data["username"], password=formUsuario.cleaned_data["password1"])
                login(request, user)
                messages.success(request, "Se ha creado el usuario correctamente")
                return redirect(to="candidatos")
            else:
                data["form"] = formUsuario
                data["formPersona"] = formPersona
                data["formAgregarEmpresa"] = formAgregarEmpresa

        return render(request, 'registration/registro.html', data)

    def settings(request):
        return render(request, 'empresa/settings.html')


class VacanteView(View):

    def get(request):
        listaVacantes = Vacante.objects.all()
        data = {
            'listaVacantes': listaVacantes
        }
        return render(request, 'vacante/listar.html', data)

    ## Agregar vacante
    def add_vacante(request):
        data = {
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
            
            formAgregarCriterio = AgregarCriterioForm(data=request.POST, instance=Criterio(vacante=vacante))
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

