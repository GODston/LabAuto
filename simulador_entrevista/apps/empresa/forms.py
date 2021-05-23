from django import forms
from django.forms import fields, widgets
from .models import Empresa, Vacante, Criterio
from django.contrib.auth.forms import UserCreationForm

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = {"empresa", "estatus", "correo"}
class AgregarEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = {"empresa", "correo"}

class VacanteForm(forms.ModelForm):

    class Meta:
        model = Vacante
        fields = {"vacante"}

class AgregarVacanteForm(forms.ModelForm):
    
    class Meta:
        model = Vacante
        fields = {"vacante", "empresa"}

class CriterioForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = '__all__'

class AgregarCriterioForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = {"criterio", "puntuacion"}

class CustomUserCreationForm(UserCreationForm):
    id