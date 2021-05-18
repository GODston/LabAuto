from django.contrib import admin
from .models import Entrevista, Pregunta, Respuesta, Grabacion, ContestaEntrevista

# Register your models here.
admin.site.register(Entrevista)
admin.site.register(Pregunta)
admin.site.register(ContestaEntrevista)
admin.site.register(Respuesta)
admin.site.register(Grabacion)

