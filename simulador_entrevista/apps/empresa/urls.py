from django.urls import path
from django.urls import path
from .views import EmpresaLoginView, EmpresaView, EmpresaRegistroView, VacantesView

urlpatterns = [
    ## Genericas
    path('login', EmpresaLoginView.get, name="inicio_sesion"),
    path('registro', EmpresaRegistroView.get, name="registro"),

    ## Configuracion
    path('configuracion', EmpresaView.get_config, name="configuracion"),

    ## Vacantes
    path('vacantes', VacantesView.get, name="vacantes"),
    path('vacantes/agregar', VacantesView.add_vacante, name="agregar_vacante"),
    path('vacantes/<int:id>', VacantesView.detail_vacante, name="detalle_vacante"),
    path('vacantes/<int:id>/eliminar', VacantesView.delete_vacante, name="eliminar_vacante"),

    ## Criterios
]