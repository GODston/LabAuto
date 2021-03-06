from django.db import models
from apps.persona.models import Persona
from apps.empresa.models import Vacante
import datetime

class Candidato(models.Model):
    CANDIDATO_ESTATUS = (
        ('A', 'Aprobado'),
        ('B', 'No Aprobado'),
        ('C', 'No Evaluado')
    )

    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=255)
    puntuacion = models.IntegerField(default=0)
    estatus = models.CharField(max_length=1, choices=CANDIDATO_ESTATUS, default='C')
    persona = models.ForeignKey(
        Persona, 
        on_delete=models.CASCADE,
        verbose_name="Referencia persona"
    )
    vacante = models.ForeignKey(
        Vacante, 
        on_delete=models.PROTECT,
        verbose_name="Vacante a la que aplica"
    )
    fechaRegistro = models.DateTimeField(default=datetime.datetime.now(), verbose_name="Fecha de registro")
    fechaEntrevista = models.DateTimeField(default=datetime.datetime.now(), verbose_name="Fecha de entrevista")

    def __str__(self):
        return self.codigo
