from django.contrib import admin
from django.urls import path
from apps.empresa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registro_empresa),
    path('empresas/', views.empresas_post),
]
