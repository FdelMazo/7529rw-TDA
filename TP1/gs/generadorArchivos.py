import random
import os

JUGADORES = "jugador"
EQUIPOS = "equipo"
EXTENSION = ".prf"

def generarArchivoPrioridades(ruta, cantidad):
    '''Recibe un nombre de archivo, una cantidad de prioridades y un directorio. Escribe prioridades aleatorias correspondientes en dicho archivo de formato .prf.'''
    prioridades = random.sample(range(cantidad), cantidad)
    with open(ruta, "w") as archivo:
        for prioridad in prioridades:
            archivo.write(str(prioridad) + "\n")

def generarLiga(cantidadJugadores, cantidadEquipos, directorio_liga = "archivos"):
    '''Recibe la cantidad de jugadores y de equipos y genera dichas cantidades de equipos y jugadores. Son guardados en la carpeta directorio_liga'''
    if not os.path.exists(directorio_liga):
        os.makedirs(directorio_liga)
    for contador in range(cantidadJugadores):
        generarSetAleatorio(os.path.join(directorio_liga, "{}_{}{}".format(JUGADOR, contador, EXTENSION)), cantidadJugadores)
    for contador in range(cantidadEquipos):
        generarSetAleatorio(os.path.join(directorio_liga, "{}_{}{}".format(EQUIPO, contador, EXTENSION)), cantidadEquipos)

