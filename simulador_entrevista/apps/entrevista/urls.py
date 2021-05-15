from django.urls import path
from .views import EntrevistaView

urlpatterns = [
    path('', EntrevistaView.get, name="entrevistas"),
    path('<int:id>', EntrevistaView.get_detail, name="detalle_entrevista")
]