from django.db import models
from apps.persona.models import Persona
from django.contrib.auth.models import User

# Create your models here.
class Empresa(models.Model):
    ESTATUS_OPCIONES = (
        ('A', 'Activo'),
        ('I', 'Inactivo')
    )

    id = models.BigAutoField(primary_key=True)
    empresa = models.CharField(max_length=255, verbose_name="Nombre de la Empresa")
    estatus = models.CharField(max_length=1, choices=ESTATUS_OPCIONES, default='A')
    correo = models.CharField(max_length=255, verbose_name="Correo de la empresa")
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        verbose_name="Referencia usuario", default='2'
    )
    persona = models.OneToOneField(
        Persona, 
        on_delete=models.CASCADE,
        verbose_name="Referencia persona"
    )

    def __str__(self):
        return self.empresa

# Tabla de vacantes
class Vacante(models.Model):
    id = models.BigAutoField(primary_key=True)
    vacante = models.CharField(max_length=255)
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE,
        verbose_name="Empresa"
    )

    def __str__(self):
        return self.vacante

# Tabla de criterio
class Criterio(models.Model):
    id = models.BigAutoField(primary_key=True)
    criterio = models.CharField(max_length=255)
    puntuacion = models.IntegerField(default=0)
    vacante = models.ForeignKey(
        Vacante, 
        on_delete=models.CASCADE,
        verbose_name="Relacion de los criterios con la vacante"
    )

    def __str__(self):
        return self.criterio
