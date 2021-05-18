from django.db import models
from apps.empresa.models import Vacante
from apps.candidato.models import Candidato
import datetime

# Tabla de entrevista relacionada con la empresa
class Entrevista(models.Model):
    id = models.BigAutoField(primary_key=True)
    alias = models.CharField(max_length=255)
    preguntas = models.IntegerField(default=0)
    fechaCreacion = models.DateTimeField(default=datetime.datetime.now())
    fechaActualizacion = models.DateTimeField(default=datetime.datetime.now())
    vacante = models.ForeignKey(
        Vacante, 
        on_delete=models.CASCADE,
        verbose_name="Vacante"
    )
    
    def __str__(self):
        return self.alias

# Tabla de preguntas, relacionadas con la entrevista
class Pregunta(models.Model):
    id = models.BigAutoField(primary_key=True)
    pregunta = models.CharField(max_length=255)
    fechaCreacion = models.DateTimeField(default=datetime.datetime.now())
    fechaActualizacion = models.DateTimeField(default=datetime.datetime.now())
    entrevista = models.ForeignKey(
        Entrevista, 
        on_delete=models.CASCADE,
        verbose_name="Entrevista"
    )

    def __str__(self):
        return self.pregunta

# Tabla para relacionar la entrevista con el candidato
class ContestaEntrevista(models.Model):
    id = models.BigAutoField(primary_key=True)
    puntuacion = models.IntegerField(default=0)
    entrevista = models.ForeignKey(
        Entrevista, 
        on_delete=models.PROTECT,
        verbose_name="Entrevista"
    )
    candidato = models.ForeignKey(
        Candidato, 
        on_delete=models.PROTECT,
        verbose_name="Candidato"
    )

    def __str__(self):
        return self.puntuacion

# Tabla en donde se guardan las respuestas
class Respuesta(models.Model):
    id = models.BigAutoField(primary_key=True)
    respuesta = models.TextField()
    contesta_entrevista = models.ForeignKey(
        ContestaEntrevista, 
        on_delete=models.PROTECT,
        verbose_name="Contestado por"
    )

    def __str__(self):
        return self.respuesta

# Tabla en donde se guardan las grabaciones
class Grabacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    archivo = models.CharField(max_length=255)
    respuesta = models.ForeignKey(
        Respuesta, 
        on_delete=models.CASCADE,
        verbose_name="Relacion con la respuesta del candidato"
    )

    def __str__(self):
        return self.archivo