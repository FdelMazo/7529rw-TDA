import os
import CrearGrilla
from Juego import Juego
from VistaJuego import VistaJuego
from Greedo import Greedo
from Dyno import Dyno

DEFAULT_GRILLA = [5, 10, (500,1000), 300] # Filas, Columnas, Rango de Vida barco, maximo danio de celda
DEFAULT_LANZADERAS = 3
ARCHIVO = 'grilla.coords'

def jugar(archivo, jugador):
    matrizTablero = Juego.ArchivoToMatriz(archivo)
    barcos = Juego.ArchivoToBarcos(archivo)
    lanzaderas = Juego.CrearLanzaderas(DEFAULT_LANZADERAS)
    
    juego = Juego(matrizTablero, barcos, lanzaderas)
    juego.setJugador(jugador)
    vista = VistaJuego(juego)
    vista.start()
    vista.update()
    while not juego.terminado():
        juego.jugar()
        vista.update()
    vista.end()
    return juego.getPuntos()

if __name__ == '__main__':
    archivo = ARCHIVO
    if not os.path.exists(archivo):
        archivo = CrearGrilla.crearArchivo(ARCHIVO, DEFAULT_GRILLA)

    greedo = Greedo() ; #dyno = Dyno()
    puntosGreedo = jugar(archivo, greedo)
    VistaJuego.imprimirSeparacion()
    #puntosDyno = jugar(archivo, dyno)
    #VistaJuego.imprimirGanador(puntosGreedo, puntosDyno)