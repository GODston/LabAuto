from django.urls import path
from .views import CodigoCandidato

urlpatterns = [
    path('', CodigoCandidato.get, name="codigo_candidato"),
    path('candidato/codigo/', CodigoCandidato.search_code, name="buscar_codigo")
]