"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
#Son las URLS generales del PROYECTO
from sistema_coder.views import saludar, saludar_con_fecha, inicio
urlpatterns= [
    path("", inicio, name="inicio"),
    path("admin/",admin.site.urls),
    path("estudios/", include("control_studios.urls")),
    # path("saludo/", saludar),
    # path("saludo-hoy/",saludar_con_fecha),
    
    

]

