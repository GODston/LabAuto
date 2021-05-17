from django import forms
from django.forms import fields, widgets
from .models import Vacante, Criterio

class VacanteForm(forms.ModelForm):

    class Meta:
        model = Vacante
        fields = '__all__'

class AgregarVacanteForm(forms.ModelForm):
    
    class Meta:
        model = Vacante
        fields = {"nombre", "empresa"}

class CriterioForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = '__all__'

class AgregarCriterioForm(forms.ModelForm):

    class Meta:
        model = Criterio
        fields = {"criterio", "puntuacion", "vacante"}