from django import forms
from django.forms import widgets
from .models import Candidato

class CandidatoForm(forms.ModelForm):

    class Meta:
        model = Candidato
        fields = '__all__'
        widgets = {
            "fechaRegistro": forms.SelectDateWidget(),
            "fechaEntrevista": forms.SelectDateWidget()
        }

class AgregarCandidatoForm(forms.ModelForm):
    
    class Meta:
        model = Candidato 
        fields = {"persona", "vacante"}
        widgets = {
            "fechaRegistro": forms.SelectDateWidget(),
            "fechaEntrevista": forms.SelectDateWidget()
        }