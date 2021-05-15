from django.urls import path
from .views import CodigoCandidatoView, CandidatoView

urlpatterns = [
    ## Candidato / Postulante
    path('', CodigoCandidatoView.get, name="codigo_candidato"),
    path('candidato/codigo', CodigoCandidatoView.search_code, name="buscar_codigo"),

    ## Candidatos vistos por la empresa
    path('candidatos', CandidatoView.get, name="candidatos"),
    path('candidatos/<int:id>', CandidatoView.get_detail, name="detalle_candidato"),
    path('candidatos/<id>/update/', CandidatoView.update_detail, name="actualizar_detalle_candidato")
]