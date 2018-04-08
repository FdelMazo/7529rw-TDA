import os
from Jugador import Jugador
from Equipo import Equipo
from generadorLigas import generarLiga

JUGADORES = "jugador"
EQUIPOS = "equipo"
EXTENSION = ".prf"
DIRECTORIO = "archivos"

def cargaDeArchivos(cantidadJugadores, cantidadEquipos, vacantes):
    '''Recibe la cantidad de jugadores y de equipos de una liga y las vacantes de cada equipo. Devuelve un diccJugadores/diccEquipos con los identificadores de cada jugador/equipo como clave y un objeto Jugador/Equipo que lo representa como valor'''
    diccJugadores = {}
    diccEquipos = {}
    for identificadorJugador in range(cantidadJugadores):
        diccJugadores[identificadorJugador] = Jugador(identificadorJugador, leerPreferencias(identificadorJugador, JUGADORES))
    for identificadorEquipo in range(cantidadEquipos):
        diccEquipos[identificadorEquipo] = Equipo(identificadorEquipo, leerPreferencias(identificadorEquipo, EQUIPOS), vacantes)
    return diccJugadores, diccEquipos

def leerPreferencias(identificador, tipo):
    '''Recibe un identificador de un objeto y su tipo. Lee las preferencias de dicho identificador y devuelve una lista con sus preferencias del tipo contrario.'''
    listaAux = []
    ruta = os.path.join(DIRECTORIO,"{}_{}{}".format(tipo, identificador, EXTENSION))
    with open(ruta,"r") as archivo:
        for linea in archivo:
            listaAux.append(int(linea.rstrip('\n')))
    return listaAux

def asignacion(diccJugadores, diccEquipos, vacantesDisponibles):
    '''Recibe un diccionario de jugadores y uno de equipos con sus respectivos objetos como valor y sus identificadores como clave y recibe la cantidad de vacantes totales disponibles entre todos los equipos. Asigna a cada objeto equipo a sus respectivos jugadores usando el algoritmo de Gale-Shapley.'''
    while vacantesDisponibles:
        for equipo in diccEquipos.values():
            while equipo.getVacantes():
                favorito = equipo.getFavorito()
                jugadorActual = diccJugadores[favorito]
                if not jugadorActual.estaAsignado():
                    equipo.agregarJugador(jugadorActual)
                    vacantesDisponibles -=1

                else:
                    equipoActual = jugadorActual.getLugarAsignado()
                    if jugadorActual.compararPreferencias(equipo, equipoActual) > 0:
                        equipoActual.quitarJugador(jugadorActual)
                        equipo.agregarJugador(jugadorActual)
                equipo.setearProximoFavorito()

def guardarAsignacion(diccEquipos, nombreArchivo):
    '''Recibe un diccionario de equipos con sus jugadores y un nombre de archivo. Escribe las asignaciones de los jugadores a dichos equipos en un archivo .txt de nombre recibido por parametro.'''
    with open(nombreArchivo,"w") as archivo:
        for numeroEquipo in diccEquipos.keys():
            archivo.write("{}:".format(numeroEquipo))
            for jugador in diccEquipos[numeroEquipo].getJugadores():
                archivo.write(" {}".format(jugador.getNumero()))
            archivo.write('\n')


def matchingGS(cantidadJugadores, cantidadEquipos, vacantesPorEquipo, archivoSalida, crearArchivos = True):
    '''Aplica el algoritmo de Gale-Shapley a una liga de equipos de Basketball y sus jugadores disponibles. Escribe un archivo txt de nombre archivoSalida recibido por parametro con los matches finales.
    Los jugadores y equipos deben estar guardados en la carpeta archivos.
    Todos los equipos y jugadores empiezan desasignados.
    Si no se le indica lo contrario, el algoritmo crea un set de prueba aleatorio de jugadores y equipos de cantidades recibidas por parametro.'''
    if crearArchivos: generarLiga(cantidadJugadores, cantidadEquipos)
    jugadores, equipos = cargaDeArchivos(cantidadJugadores, cantidadEquipos, vacantesPorEquipo)
    asignacion(jugadores, equipos, cantidadEquipos * vacantesPorEquipo)
    guardarAsignacion(equipos, archivoSalida)
    return jugadores, equipos
