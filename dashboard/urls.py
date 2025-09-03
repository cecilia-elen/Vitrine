# Dentro do arquivo usuario/urls.py

from django.urls import path
from . import views

# Isso ajuda a organizar e evitar conflito de nomes de URLs
app_name = 'dashboard'

urlpatterns = [

    path('Controle_adm_usuarios/', views.Controle_adm_usuarios, name="Controle_adm_usuarios"),
]