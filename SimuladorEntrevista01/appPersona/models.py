from django.db import models

class Persona(models.Model):
    SEXO_OPCIONES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    )

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES)
    correo = models.CharField(max_length=60)
    telefono = models.CharField(max_length=14)
    celular = models.CharField(max_length=14)

    def __init__(self, id, nombre, puesto, edad, fechaRegistro, fechaEntrevista):
        self.id=id
        self.nombre=nombre
        self.puesto=puesto
        self.edad=edad
        self.fechaRegistro=fechaRegistro
        self.fechaEntrevista=fechaEntrevista
