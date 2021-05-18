from django.urls import path
from .views import EntrevistaView, PreguntasView

urlpatterns = [
    ## Entrevista
    path('', EntrevistaView.list, name="entrevistas"), ## Obtiene lista
    path('agregar', EntrevistaView.add_entrevista, name="agregar_entrevista"), ## Obtiene formulario y agrega
    path('<int:id>', EntrevistaView.detail_entrevista, name="detalle_entrevista"), ## Obtiene detalle y actualiza
    path('<int:id>/eliminar', EntrevistaView.delete_entrevista, name="eliminar_entrevista"), ## Elimina la entrevista

    ## Preguntas
    path('<int:entrevista_id>/preguntas/<int:pregunta_id>/eliminar', PreguntasView.delete_pregunta, name="eliminar_pregunta"), ## Elimina la pregunta
]