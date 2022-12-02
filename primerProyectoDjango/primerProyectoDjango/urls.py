"""primerProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from clientes.views import aniadir_clientes, delete_client_template, delete_client
from deportes.views import deportes, listar_selecciones, aniadir_seleccion, listar_jugadores, aniadir_jugadores, \
    eliminar_jugador, editar_jugador, actualizar_jugador
from webapp.views import bienvenido, despedida, listar_alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name="inicio"),
    path('good_bye/', despedida),
    path('deportes/', deportes, name="deportes"),
    path('alumnos/listado_alumnos/', listar_alumnos, name="listado_alumnos"),
    path('deportes/futbol/listado-selecciones', listar_selecciones, name="listado_selecciones"),
    path('deportes/futbol/aniadir-seleccion', aniadir_seleccion, name="aniadir_seleccion"),
    path('clientes/nuevo_cliente', aniadir_clientes, name="aniadir_cliente"),
    path('clientes/delete_template', delete_client_template, name="clientes_del_template"),
    path('clientes/delete/<int:id>', delete_client, name="client_del"),
    path('deportes/futbol/listado-jugadores', listar_jugadores, name="listado_jugadores"),
    path('deportes/futbol/listado-jugadores/add-player', aniadir_jugadores, name="aniadir_jugador"),
    path('deportes/futbol/eliminar-jugador/<int:id>', eliminar_jugador, name="eliminar_jugador"),
    path('deportes/futbol/listado-jugadores/edit-player/<int:id>', editar_jugador, name="editar_jugador"),
    path('deportes/futbol/listado-jugadores/update-player/<int:id>', actualizar_jugador, name="actualizar_jugador"),
]
