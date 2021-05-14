from django.db import models
from apps.persona.models import Persona
from apps.empresa.models import Vacante

class Candidato(models.Model):
    CANDIDATO_ESTATUS = (
        ('A', 'Aprobado'),
        ('B', 'No Aprobado'),
        ('C', 'No Evaluado')
    )

    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=255)
    puntuacion = models.IntegerField()
    estatus = models.CharField(max_length=1, choices=CANDIDATO_ESTATUS)
    persona = models.ForeignKey(
        Persona, 
        on_delete=models.CASCADE,
        verbose_name="Relacion del candidato con informacion de persona"
    )
    vacante = models.ForeignKey(
        Vacante, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de candidato con la vacante"
    )
