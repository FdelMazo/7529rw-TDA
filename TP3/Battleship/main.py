import os
import platform
import CrearGrilla
from Juego import Juego
from VistaJuego import VistaJuego
from Greedo import Greedo
from Dyno import Dyno
import argparse

DEFAULT_GRILLA = [5, 10, (500, 1000), 300]  # Filas, Columnas, Rango de Vida barco, maximo danio de celda
DEFAULT_LANZADERAS = 2
ARCHIVO = 'grilla.coords'


def jugar(archivo, jugador, no_input, sistema):
    matrizTablero = Juego.ArchivoToMatriz(archivo)
    barcos = Juego.ArchivoToBarcos(archivo)
    cantidadLanzaderas = DEFAULT_LANZADERAS

    juego = Juego(matrizTablero, barcos, cantidadLanzaderas, jugador)
    juego.setPosicionesIniciales()
    vista = VistaJuego(juego, no_input, sistema)
    vista.start()
    while not juego.terminado():
        juego.elegirTargets()
        vista.informacionTurno()
        vista.imprimirMapa()
        juego.jugarTurno()
    vista.informacionTurno()
    vista.imprimirMapa()
    vista.end()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--no-input', help='Deshabilitar el input del usuario', action='store_true')
    parser.add_argument('-o', '--overwrite', help='Sobreescribe el mapa al comenzar la ejecución', action='store_true')
    args = parser.parse_args()
    archivo = ARCHIVO
    if not os.path.exists(archivo) or args.overwrite:
        archivo = CrearGrilla.crearArchivo(ARCHIVO, DEFAULT_GRILLA)
    greedo = Greedo()
    dyno = Dyno()
    VistaJuego.titulo(platform.system())
    jugar(archivo, greedo, args.no_input, platform.system())
    VistaJuego.imprimirSeparacion(platform.system())
    jugar(archivo, dyno, args.no_input, platform.system())
    VistaJuego.imprimirGanador(greedo, dyno, platform.system())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass  # Exit smoothly
