from django.db import models

# Revisar si es posible utilizar una tabla de personas para almacenar los datos genericos
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
        

# Tabla de empresas
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

# Tabla donde se almacena el candidato
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