from django.urls import path
from .views import CodigoCandidatoView, CandidatoView

urlpatterns = [
    ## Candidato / Postulante
    path('', CodigoCandidatoView.search_code, name="buscar_codigo"),
    path('candidato/<int:id>/bienvenido', CodigoCandidatoView.welcome_entrevista, name="bienvenida_entrevista"),
    path('candidato/<int:id>/entrevista', CodigoCandidatoView.init_entrevista, name="inicio_entrevista"),
    path('candidato/<int:id>/entrevista/guardar', CodigoCandidatoView, name="guardar_entrevista"),

    ## Candidatos vistos por la empresa
    path('candidatos', CandidatoView.get, name="candidatos"),
    path('candidatos/agregar', CandidatoView.add_candidato, name="agregar_candidato"),
    path('candidatos/<int:id>', CandidatoView.detail_candidato, name="detalle_candidato"),
    path('candidatos/<int:id>/eliminar', CandidatoView.delete_candidato, name="eliminar_candidato"),
]