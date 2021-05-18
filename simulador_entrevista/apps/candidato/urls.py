from django.urls import path
from .views import CodigoCandidatoView, CandidatoView

urlpatterns = [
    ## Candidato / Postulante
    path('', CodigoCandidatoView.get, name="codigo_candidato"),
    path('candidato/codigo', CodigoCandidatoView.search_code, name="buscar_codigo"),

    ## Candidatos vistos por la empresa
    path('candidatos', CandidatoView.get, name="candidatos"),
    path('candidatos/agregar', CandidatoView.add_candidato, name="agregar_candidato"),
    path('candidatos/<int:id>', CandidatoView.detail_candidato, name="detalle_candidato"),
    path('candidatos/<int:id>/eliminar', CandidatoView.delete_candidato, name="eliminar_candidato"),
]