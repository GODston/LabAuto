from django import forms
from django.forms import widgets
from .models import Candidato

class CandidatoForm(forms.ModelForm):

    class Meta:
        model = Candidato
        fields = {"fechaEntrevista", "fechaRegistro", "vacante", "estatus", "puntuacion", "codigo"}
        widgets = {
            "fechaRegistro": forms.SelectDateWidget(),
            "fechaEntrevista": forms.SelectDateWidget()
        }

class AgregarCandidatoForm(forms.ModelForm):
    
    class Meta:
        model = Candidato 
        fields = {"vacante"}
        widgets = {
            "fechaRegistro": forms.SelectDateWidget(),
            "fechaEntrevista": forms.SelectDateWidget()
        }

class CodigoCandidato(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = {"codigo"}