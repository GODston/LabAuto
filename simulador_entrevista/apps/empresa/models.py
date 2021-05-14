from django.db import models
from apps.persona.models import Persona

# Create your models here.
class Empresa(models.Model):
    ESTATUS_OPCIONES = (
        ('A', 'Activo'),
        ('I', 'Inactivo')
    )

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    estatus = models.CharField(max_length=1, choices=ESTATUS_OPCIONES)
    correo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    persona = models.OneToOneField(
        Persona, 
        on_delete=models.CASCADE,
        verbose_name="Persona relacionada con la empresa"
    )

# Tabla de vacantes
class Vacante(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de la vacante con la empresa"
    )

# Tabla de criterio
class Criterio(models.Model):
    id = models.BigAutoField(primary_key=True)
    criterio = models.CharField(max_length=255)
    puntuacion = models.IntegerField()
    vacante = models.ForeignKey(
        Vacante, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de los criterios con la vacante"
    )
