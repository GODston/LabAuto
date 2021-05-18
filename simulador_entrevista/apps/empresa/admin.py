from django.contrib import admin
from .models import Empresa, Vacante, Criterio

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Vacante)
admin.site.register(Criterio)