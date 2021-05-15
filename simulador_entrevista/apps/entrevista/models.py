from django.db import models
from apps.empresa.models import Vacante
from apps.candidato.models import Candidato

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
    
    def __str__(self):
        return self.alias

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

    def __str__(self):
        return self.pregunta

# Tabla para relacionar la entrevista con el candidato
class ContestaEntrevista(models.Model):
    id = models.BigAutoField(primary_key=True)
    puntuacion = models.IntegerField()
    entrevista = models.ForeignKey(
        Entrevista, 
        on_delete=models.PROTECT,
        verbose_name="Relacion de respuestas con la entrevista"
    )
    candidato = models.ForeignKey(
        Candidato, 
        on_delete=models.PROTECT,
        verbose_name="Relacion de respuestas con candidato"
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
        verbose_name="Relacion con contestacion entrevistado"
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