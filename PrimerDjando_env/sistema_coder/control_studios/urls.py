#URLS específicas de LA APP

from django.contrib import admin
from django.urls import path
#Son las URLS generales del PROYECTO
from control_studios.views import listar_estudiantes, listar_cursos
urlpatterns= [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("cursos/", listar_cursos, name="lista_cursos"),
]
