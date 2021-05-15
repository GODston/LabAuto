from django.urls import path
from django.urls import path
from .views import EmpresaLogin, Empresa, EmpresaRegistro

urlpatterns = [
    path('login', EmpresaLogin.get, name="inicio_sesion"),
    path('registro', EmpresaRegistro.get, name="registro"),
    path('configuracion', Empresa.get_config, name="configuracion"),
]