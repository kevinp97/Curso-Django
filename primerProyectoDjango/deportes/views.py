from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404

from deportes.models import Jugadores


# Create your views here.
def deportes(request):
    contenido = {"titulo_pagina": "Actualidad deportiva",
                 "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
    return render(request, "deportes.html", contenido)


def listar_selecciones(request):
    espania = {"nombre": "España", "continente": "Europa", "num_mundiales": 1}
    brasil = {"nombre": "Brasil", "continente": "America", "num_mundiales": 5}
    francia = {"nombre": "Francia", "continente": "Europa", "num_mundiales": 2}
    senegal = {"nombre": "Senegal", "continente": "Africa", "num_mundiales": 0}

    lista_selecciones = [espania, brasil, francia, senegal]

    #Miro si tengo datos en la sesion
    listado_seleccion = request.session.get("listado_selecciones", None)

    #Si en la sesion no hay nada
    if listado_seleccion == None:
        request.session['listado_selecciones'] = lista_selecciones
        listado_seleccion = lista_selecciones



    continente_filtro = None
    if request.method == 'POST':
        titulo = "hola"
        accion = request.POST.get('action', '')

        if accion == "filtrar":
            continente_filtro = request.POST['continente']
            titulo = request.POST.get('titulo', 'Titulo por Defecto')

            listado_seleccion = list(
                filter(lambda seleccion: seleccion["continente"] == continente_filtro, listado_seleccion))

        elif accion == "guardar":
            nombre = request.POST["nombre"]
            continente = request.POST["continente"]
            num_mundiales = request.POST["mundiales"]
            #Creo diccionario con los datos que mandan
            nueva_seleccion = {"nombre": nombre, "continente": continente, "num_mundiales": num_mundiales}
            listado_seleccion.append(nueva_seleccion)

            request.session['listado_selecciones'] = listado_seleccion

            titulo = request.POST.get('titulo', 'Titulo por Defecto')

    elif request.method == 'GET':
        # titulo = request.parameter("titulo")
        # titulo = request.GET['titulo']
        titulo = request.GET.get('titulo', 'Titulo por Defecto')


    contexto = {"listado_selecciones": listado_seleccion, "titulo_tabla": titulo,
                "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}

    return render(request, "selecciones_mundial.html", contexto)


def aniadir_seleccion(request):
    return render(request, "nueva_seleccion.html")

def listar_jugadores(request):
    posiciones = ['Portero', 'Defensa centra','Lateral izquierdo','Lateral derecho',
                            'Centrocampista defensivo', 'Medio centro', 'Media punta', 'Extremo izquierdo',
                            'Extremo derecho', 'Delantero']
    nacionalidad = ['España', 'Portugal', 'Alemania','Francia','Italia','Inglaterra','Argentina','Brasil','Uruguay']
    equipos = ['Real Madrid', 'FC Barcelona', 'Atletico de Madrid','Sevilla','Betis', 'Bayern de Munich', 'BVB',
               'PSG', 'Juventus', 'Milan', 'Inter Milan', 'Roma', 'Napoles', 'Liverpool', 'Manchester United',
               'Manchester City', 'Arsenal', 'Chelsea']

    jugadores = Jugadores.objects.all()
    contexto = {"listado_posicion": posiciones, "listado_nacionalidad": nacionalidad,
                "listado_equipos":equipos, "jugadores":jugadores}

    return render(request, 'jugadores.html', contexto)

JugadorForm = modelform_factory(Jugadores, exclude=[])
def aniadir_jugadores(request):
    mensaje = ''
    if request.method == 'POST':
        jugador_form = JugadorForm(request.POST)
        jugador_form.save()
        mensaje = 'Jugador registrado en la base de datos'
    jugador_form = JugadorForm()
    contexto = {"mensaje":mensaje, "jugador_form":jugador_form}
    return render(request, 'add_jugador.html', contexto)

def eliminar_jugador(request, id):
    jugador = Jugadores.objects.get(pk=id)
    jugador.delete()
    jugadores = Jugadores.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request, 'jugadores.html', contexto)

def editar_jugador(request, id):
    mensaje = ''
    if request.method == 'POST':
        mensaje = 'Jugador actualizado en la base de datos'

    jugador = Jugadores.objects.filter(id=id).first()
    jugador_form = JugadorForm(instance=jugador)
    contexto = {"jugador_form": jugador_form, "jugador":jugador, "mensaje":mensaje}
    return render(request, "edit_jugador.html", contexto)

def actualizar_jugador(request, id):
    jugador = Jugadores.objects.get(pk=id)
    #obtener los datos de la edicion del jugador y hacer match con el jugador de la base de datos
    jugador_form = JugadorForm(request.POST, instance=jugador)
    if jugador_form.is_valid():
        jugador_form.save()
    jugadores = Jugadores.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request,"jugadores.html",contexto)