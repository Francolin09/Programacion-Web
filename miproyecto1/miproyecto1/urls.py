"""miproyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from miproyecto1.views import bienvenida
from miproyecto1.views import bienvenidaenrojo
from miproyecto1.views import categoriaEdad
from miproyecto1.views import obtenerMomento
from miproyecto1.views import obtenerMomentobonito
from miproyecto1.views import contenidoHTML
from miproyecto1.views import primeraplantilla
from miproyecto1.views import plantillaParametros
from miproyecto1.views import plantillaListasBucles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/',bienvenida),
    path('bienvenida123',bienvenidaenrojo),
    path('categoriaEdad/<int:edad>', categoriaEdad),#pasando parametros en la url en este caso la edad pero antes se debe convertir en entero
    path('momento', obtenerMomento),
    path('momentonito', obtenerMomentobonito),
    path('html/<nombre>/<int:edad>',contenidoHTML),
    path('plantilla',primeraplantilla),
    path('plantillaParametros',plantillaParametros),
    path('plantillaLista',plantillaListasBucles),
]
