import random
def generarSetAleatorio(nombre, lista, cantidad):
    arreglo = random.sample(lista, cantidad)
    file = open(nombre,"w")
    str_arreglo = ''.join(str(arreglo))
    preferencias = str_arreglo.replace('[','').replace(']','')
    file.write(preferencias)
    file.close()

def generarArchivos(nombreArchivoJugadores, extensionArchivoJugadores, cantidadJugadores, nombreArchivoEquipos, extensionArchivoEquipos, cantidadEquipos):
    lista_equipos = []
    for i in range(cantidadEquipos):
        lista_equipos.append(i + 1)

    lista_jugadores = []
    for i in range(cantidadJugadores):
        lista_jugadores.append(i + 1)

    for i in range(cantidadEquipos):
        generarSetAleatorio(nombreArchivoEquipos + str(i + 1) + extensionArchivoJugadores, lista_jugadores, cantidadJugadores)
        
    for i in range(cantidadJugadores):
        generarSetAleatorio(nombreArchivoJugadores + str(i + 1) + extensionArchivoEquipos, lista_equipos, cantidadEquipos)
        
