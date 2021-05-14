from django.urls import path
from django.urls import path
from .views import EmpresaLogin

urlpatterns = [
    path('login/', EmpresaLogin.get, name="login"),
]