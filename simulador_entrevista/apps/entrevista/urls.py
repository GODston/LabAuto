from django.urls import path
from .views import EntrevistaView, PreguntasView

urlpatterns = [
    ## Entrevista
    path('', EntrevistaView.list, name="entrevistas"), ## Obtiene lista
    path('agregar', EntrevistaView.add_entrevista, name="agregar_entrevista"), ## Obtiene formulario y agrega
    path('<int:id>', EntrevistaView.detail_entrevista, name="detalle_entrevista"), ## Obtiene detalle y actualiza
    path('<int:id>/eliminar', EntrevistaView.delete_entrevista, name="eliminar_entrevista"), ## Elimina la entrevista

    ## Preguntas
    ##path('<int:id>/preguntas', PreguntasView.list, name="preguntas"), ## Obtiene lista de preguntas
    ##path('preguntas/agregar', PreguntasView.add_pregunta, name="agregar_pregunta"), ## Agrega pregunta
    ## path('<int:id>/preguntas/<int:pregunta_id>', PreguntasView.update_pregunta, name="actualizar_pregunta"), ## Actualiza la pregunta
    path('preguntas/<int:id>/eliminar', PreguntasView.delete_pregunta, name="eliminar_pregunta"), ## Elimina la pregunta
]