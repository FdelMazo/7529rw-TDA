import random
import os

JUGADOR = "jugador"
EQUIPO = "equipo"
EXTENSION = ".prf"
DIRECTORIO = "archivos"

def generarArchivoPrioridades(ruta, cantidad):
    '''Recibe un nombre de archivo, una cantidad de prioridades y un directorio. Escribe prioridades aleatorias correspondientes en dicho archivo de formato .prf.'''
    prioridades = random.sample(range(cantidad), cantidad)
    with open(ruta, "w") as archivo:
        for prioridad in prioridades:
            archivo.write(str(prioridad) + "\n")

def generarLiga(cantidadJugadores, cantidadEquipos):
    '''Recibe la cantidad de jugadores y de equipos y genera dichas cantidades de equipos y jugadores. Son guardados en la carpeta directorio_liga'''
    for contador in range(cantidadJugadores):
        generarArchivoPrioridades(os.path.join(DIRECTORIO, "{}_{}{}".format(JUGADOR, contador, EXTENSION)), cantidadEquipos)
    for contador in range(cantidadEquipos):
        generarArchivoPrioridades(os.path.join(DIRECTORIO, "{}_{}{}".format(EQUIPO, contador, EXTENSION)), cantidadJugadores)

#generarLiga(200, 20)
