from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('about', views.about),
    path('interviews', views.interviews),
    path('interviews/<int:id>/', views.interview_details),
    path('candidates', views.candidates),
    path('candidates/<int:id>/', views.candidate_details),
    path('settings', views.settings)
    path('act_login/' views.act_login)
]
