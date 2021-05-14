from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.candidato.urls')),
    path('empresas/', include('apps.empresa.urls')),
    path('nosotros/', about, name="nosotros"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
