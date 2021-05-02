from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = '/login'),
    path('register', views.register, name = '/register'),
    path('about', views.about, name = '/about'),
    path('interviews', views.interviews, name = '/interviews'),
    path('interviews/<int:id>/', views.interview_details),
    path('candidates', views.candidates, name = '/candidates'),
    path('settings', views.settings, name = '/settings')
]
