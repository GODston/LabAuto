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

    def __str__(self):
        return self.nombre + " " + self.ap_paterno + " " + self.ap_materno
