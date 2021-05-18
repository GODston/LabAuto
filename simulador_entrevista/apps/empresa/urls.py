from django.urls import path
from django.urls import path
from .views import EmpresaView, VacanteView, CriterioView

urlpatterns = [
    ## Sesion / Usuario
    path('login', EmpresaView.login, name="inicio_sesion"),
    path('registro', EmpresaView.register, name="registro"),
    path('configuracion', EmpresaView.settings, name="configuracion"),

    ## Vacantes
    path('vacantes', VacanteView.get, name="vacantes"),
    path('vacantes/agregar', VacanteView.add_vacante, name="agregar_vacante"),
    path('vacantes/<int:id>', VacanteView.detail_vacante, name="detalle_vacante"),
    path('vacantes/<int:id>/eliminar', VacanteView.delete_vacante, name="eliminar_vacante"),

    ## Criterios
    path('vacantes/<int:vacante_id>/criterios/<int:criterio_id>/eliminar', CriterioView.delete_criterio, name="eliminar_criterio"),
]