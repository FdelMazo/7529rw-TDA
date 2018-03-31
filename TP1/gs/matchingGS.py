from Jugador import Jugador
from Equipo import Equipo
import random


def generarSetAleatorio(nombre, lista, cantidad):
    arreglo = random.sample(lista, cantidad) #O(cantidad)
    file = open(nombre,"w") #O(1)
    file.write(str(arreglo[0])) #O(1)
    for i in range(1, len(arreglo)):#O(cantidad)
        file.write('\n' + str(arreglo[i])) 
    file.close() #O(1)

def generarArchivos(nombreArchivoJugadores, extensionArchivoJugadores, cantidadJugadores, nombreArchivoEquipos, extensionArchivoEquipos, cantidadEquipos):
    lista_equipos = [] #O(1)
    for i in range(cantidadEquipos): #O(cantidadEquipos)
        lista_equipos.append(i + 1)

    lista_jugadores = [] #O(1)
    for i in range(cantidadJugadores): #O(cantidadJugadores)
        lista_jugadores.append(i + 1)

    for i in range(cantidadEquipos): #O(cantidadEquipos * cantidadDeJugadores)
        generarSetAleatorio(nombreArchivoEquipos + str(i + 1) + extensionArchivoJugadores, lista_jugadores, cantidadJugadores)
        
    for i in range(cantidadJugadores): #O(cantidadEquipos * cantidadDeJugadores)
        generarSetAleatorio(nombreArchivoJugadores + str(i + 1) + extensionArchivoEquipos, lista_equipos, cantidadEquipos)
        

def cargaDeArchivos(jugadores, equipos, nombreArchivoJugadores, extensionArchivoJugadores, nombreArchivoEquipos, extensionArchivoEquipos, cantidadJugadores, cantidadEquipos, vacantesPorEquipo):
    
    listaAux = []
    for i in range(cantidadJugadores): #O(cantidadJugadores * cantidadEquipos)
        numeroJugador = i + 1 #O(1)
        with open(nombreArchivoJugadores + str(numeroJugador) + extensionArchivoJugadores,"r") as archivo: #O(1)
            for linea in archivo: #O(cantidadEquipos)
                listaAux.append(int(linea.rstrip('\n')))
        archivo.close() #O(1)
        jugadores[numeroJugador] =  Jugador(numeroJugador, listaAux) #O(1)
        
    listaAux = []
    for i in range(cantidadEquipos): #O(cantidadJugadores * cantidadEquipos)
        numeroEquipo = i + 1 #O(1)
        with open(nombreArchivoEquipos + str(numeroEquipo) + extensionArchivoEquipos,"r") as archivo: #O(1)
            for linea in archivo: #O(cantidadJugadores)
                listaAux.append(int(linea.rstrip('\n')))
        archivo.close() #O(1)
        equipos[numeroEquipo] =  Equipo(numeroEquipo, listaAux, vacantesPorEquipo) #O(1)


def asignacion(jugadores, equipos, cantidadEquipos, vacantesPorEquipo):
    vacantesEnEquipos = cantidadEquipos * vacantesPorEquipo
    
    '''Mientras haya un equipo con vacantes.'''
    while vacantesEnEquipos: #O(J*E)
        for nro, e in equipos.items():
            while e.getVacantes():
                '''El equipo actual ofrece una vacante a su jugador favorito actual'''
                numerojugadorActual = e.getFavorito() #O(1)
                jugadorActual = jugadores[numerojugadorActual] #O(1)
                
                '''Si el jugador esta libre, acepta la vacante'''
                if not jugadorActual.estaAsignado(): #O(1)
                    e.agregarJugador(jugadorActual) #O(1)
                    vacantesEnEquipos -=1 #O(1)
                                
                else:
                    '''Si no esta libre, pero prefiere más al equipo actual, acepta la vacante
                    y el otro equipo pierde a ese jugador.'''
                    if jugadorActual.compararPreferencias(e.getNumero(), jugadorActual.getLugarAsignado().getNumero()) > 0: #O(1)
                        jugadorActual.getLugarAsignado().quitarJugador(jugadorActual) #O(1)
                        e.agregarJugador(jugadorActual) #O(1)
                        
                e.setearProximoFavorito() #O(1)


def guardarAsignacion(equipos, nombreArchivo):
    with open(nombreArchivo,"w") as archivo: #O(1)
        for nro, e in equipos.items(): #O(J*E)
            archivo.write(str(nro) + ':')
            
            for j in e.jugadores:
                archivo.write(' ' + str(j.getNumero()))
            archivo.write('\n')
    
    archivo.close()
    

def matchingGS(nombreArchivoJugadores, extensionArchivoJugadores, nombreArchivoEquipos, extensionArchivoEquipos, archivoSalida, cantidadJugadores, cantidadEquipos, vacantesPorEquipo, crearArchivos):
    '''Todos los equipos y jugadores empiezan desasignados'''
    equipos = {} #O(1)
    jugadores = {} #O(1)
    if crearArchivos.lower()=='y': #O(1)
        generarArchivos(nombreArchivoJugadores, extensionArchivoJugadores, cantidadJugadores, nombreArchivoEquipos, extensionArchivoEquipos, cantidadEquipos) #O(cantidadJugadores * cantidadEquipos)
    cargaDeArchivos(jugadores, equipos, nombreArchivoJugadores, extensionArchivoJugadores, nombreArchivoEquipos, extensionArchivoEquipos, cantidadJugadores, cantidadEquipos, vacantesPorEquipo) #O(cantidadJugadores * cantidadEquipos)
    asignacion(jugadores, equipos, cantidadEquipos, vacantesPorEquipo)
    guardarAsignacion(equipos, archivoSalida)
