from django.db import models
from appEmpresa.models import Vacante
from appCandidato.models import Candidato

# Tabla de entrevista relacionada con la empresa
class Entrevista(models.Model):
    id = models.BigAutoField(primary_key=True)
    alias = models.CharField(max_length=255)
    preguntas = models.IntegerField()
    fechaCreacion = models.DateTimeField()
    fechaActualizacion = models.DateTimeField()
    vacante = models.ForeignKey(
        Vacante, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de la entrevista con la vacante"
    )

    def __init__(self, id, alias, fechaCreacion, fechaActualizacion, preguntas):
        self.id=id
        self.alias=alias
        self.fechaCreacion=fechaCreacion
        self.fechaActualizacion=fechaActualizacion
        self.preguntas=preguntas

# Tabla de preguntas, relacionadas con la entrevista
class Pregunta(models.Model):
    id = models.BigAutoField(primary_key=True)
    pregunta = models.CharField(max_length=255)
    fechaCreacion = models.DateTimeField()
    fechaActualizacion = models.DateTimeField()
    entrevista = models.ForeignKey(
        Entrevista, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de la pregunta con la entrevista"
    )

    def __init__(self, id, pregunta):
        self.id=id
        self.pregunta=pregunta

# Tabla para relacionar la entrevista con el candidato
class ContestaEntrevista(models.Model):
    id = models.BigAutoField(primary_key=True)
    puntuacion = models.IntegerField()
    entrevista = models.ForeignKey(
        Entrevista, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de respuestas con la entrevista"
    )
    candidato = models.ForeignKey(
        Candidato, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de respuestas con candidato"
    )

# Tabla en donde se guardan las respuestas
class Respuesta(models.Model):
    id = models.BigAutoField(primary_key=True)
    respuesta = models.TextField()
    contesta_entrevista = models.ForeignKey(
        ContestaEntrevista, 
        on_delete=models.CASCADE,
        verbose_name="Relacion con contestacion entrevistado"
    )

# Tabla en donde se guardan las grabaciones
class Grabacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    archivo = models.CharField(max_length=255)
    respuesta = models.ForeignKey(
        Respuesta, 
        on_delete=models.CASCADE,
        verbose_name="Relacion con la respuesta del candidato"
    )