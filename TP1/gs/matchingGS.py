from Jugador import Jugador
from Equipo import Equipo
from generarLigas import generarLiga
from generarLigas import EXTENSION

def cargaDeArchivos(jugadores, equipos, nombreArchivoJugadores, nombreArchivoEquipos, cantidadJugadores, cantidadEquipos, vacantesPorEquipo):
    
    listaAux = []
    for i in range(cantidadJugadores): #O(cantidadJugadores * cantidadEquipos)
        numeroJugador = i + 1 #O(1)
        with open(nombreArchivoJugadores + str(numeroJugador) + EXTENSION,"r") as archivo: #O(1)
            for linea in archivo: #O(cantidadEquipos)
                listaAux.append(int(linea.rstrip('\n')))
        archivo.close() #O(1)
        jugadores[numeroJugador] =  Jugador(numeroJugador, listaAux) #O(1)
        
    listaAux = []
    for i in range(cantidadEquipos): #O(cantidadJugadores * cantidadEquipos)
        numeroEquipo = i + 1 #O(1)
        with open(nombreArchivoEquipos + str(numeroEquipo) + EXTENSION,"r") as archivo: #O(1)
            for linea in archivo: #O(cantidadJugadores)
                listaAux.append(int(linea.rstrip('\n')))
        archivo.close() #O(1)
        equipos[numeroEquipo] =  Equipo(numeroEquipo, listaAux, vacantesPorEquipo) #O(1)


def asignacion(diccJugadores, diccEquipos, cantidadEquipos, vacantesPorEquipo):
    vacantesEnEquipos = cantidadEquipos * vacantesPorEquipo
    
    '''Mientras haya un equipo con vacantes.'''
    while vacantesEnEquipos: #O(J*E)
        for numero, equipo in dicEquipos.items():
            while equipo.getVacantes():
                '''El equipo actual ofrece una vacante a su jugador favorito actual'''
                numerojugadorActual = equipo.getFavorito() #O(1)
                jugadorActual = diccJugadores[numerojugadorActual] #O(1)
                
                '''Si el jugador esta libre, acepta la vacante'''
                if not jugadorActual.estaAsignado(): #O(1)
                    equipo.agregarJugador(jugadorActual) #O(1)
                    vacantesEnEquipos -=1 #O(1)
                                
                else:
                    '''Si no esta libre, pero prefiere más al equipo actual, acepta la vacante
                    y el otro equipo pierde a ese jugador.'''
                    if jugadorActual.compararPreferencias(equipo.getNumero(), jugadorActual.getLugarAsignado().getNumero()) > 0: #O(1)
                        jugadorActual.getLugarAsignado().quitarJugador(jugadorActual) #O(1)
                        equipo.agregarJugador(jugadorActual) #O(1)
                        
                equipo.setearProximoFavorito() #O(1)


def guardarAsignacion(diccEquipos, nombreArchivo):
    '''Recibe un diccionario de equipos con sus jugadores y un nombre de archivo. Escribe las asignaciones de los jugadores a dichos equipos en un archivo .txt de nombre recibido por parametro.'''
    with open(nombreArchivo,"w") as archivo: #O(1)
        for numeroEquipo in diccEquipos.keys(): #O(J*E)
            archivo.write("{}:".format(numeroEquipo))
            for jugador in diccEquipos[numeroEquipo].getJugadores():
                archivo.write(" {}".format(jugador.getNumero()))
            archivo.write('\n')
    

def matchingGS(cantidadJugadores, cantidadEquipos, vacantesPorEquipo, archivoSalida, crearArchivos = True):
    '''Aplica el algoritmo de Gale-Shapley a una liga de equipos de Basketball y sus jugadores disponibles. Escribe un archivo txt de nombre archivoSalida recibido por parametro con los matches finales.
    Los jugadores y equipos deben estar guardados en la carpeta archivos.
    Todos los equipos y jugadores empiezan desasignados.
    Si no se le indica lo contrario, el algoritmo crea un set de prueba aleatorio de jugadores y equipos de cantidades recibidas por parametro.'''
    equipos = {} #O(1)
    jugadores = {} #O(1)
    if crearArchivos: #O(1)
        generarLiga(cantidadJugadores, cantidadEquipos) #O(cantidadJugadores * cantidadEquipos)
    cargaDeArchivos(jugadores, equipos, nombreArchivoJugadores, nombreArchivoEquipos, cantidadJugadores, cantidadEquipos, vacantesPorEquipo) #O(cantidadJugadores * cantidadEquipos)
    asignacion(jugadores, equipos, cantidadEquipos, vacantesPorEquipo)
    guardarAsignacion(equipos, archivoSalida)
