from django import forms
from django.forms import fields, widgets
from .models import Entrevista, Pregunta, Respuesta

class AgregarEntrevistaForm(forms.ModelForm):

    class Meta:
        model = Entrevista
        fields = {'alias', 'vacante'}

class AgregarPreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = {'pregunta'}

class EntrevistaForm(forms.ModelForm):
    
    class Meta:
        model = Entrevista
        fields = '__all__'
        widgets = {
            "fechaCreacion": forms.SelectDateWidget(),
            "fechaActualizacion": forms.SelectDateWidget()
        }

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = '__all__'