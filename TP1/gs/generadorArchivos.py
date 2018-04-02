import random

ARCHIVO_JUGADORES = "jugador"
ARCHIVO_EQUIPOS = "equipo"
EXTENSION = ".prf"

def generarSetAleatorio(nombre_archivo, cantidad):
    prioridades = random.sample(range(cantidad), cantidad)
    with open(nombre_archivo, "w") as archivo:
        for prioridad in prioridades:
            archivo.write(str(prioridad) + "\n")

def generarArchivos(cantidadJugadores, cantidadEquipos):
    for contador in range(cantidadJugadores):
        generarSetAleatorio("{}_{}{}".format(ARCHIVO_JUGADORES, contador, EXTENSION), cantidadJugadores)
    for contador in range(cantidadEquipos):
        generarSetAleatorio("{}_{}{}".format(ARCHIVO_EQUIPOS, contador, EXTENSION), cantidadEquipos)
