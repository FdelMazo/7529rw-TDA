import os
import CrearGrilla
from Juego import Juego
from VistaJuego import VistaJuego
from Greedo import Greedo
from Dyno import Dyno
import argparse

DEFAULT_GRILLA = [5, 10, (500,1000), 300] # Filas, Columnas, Rango de Vida barco, maximo danio de celda
DEFAULT_LANZADERAS = 3
ARCHIVO = 'grilla.coords'


def jugar(archivo, jugador, no_input):
	matrizTablero = Juego.ArchivoToMatriz(archivo)
	barcos = Juego.ArchivoToBarcos(archivo)
	cantidadLanzaderas = DEFAULT_LANZADERAS

	juego = Juego(matrizTablero, barcos, cantidadLanzaderas, jugador)
	juego.setPosicionesIniciales()
	vista = VistaJuego(juego, no_input)
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
	parser.add_argument('--no-input',help='Deshabilitar el input del usuario', action = 'store_true')
	args = parser.parse_args()
	archivo = ARCHIVO
	if not os.path.exists(archivo):
		archivo = CrearGrilla.crearArchivo(ARCHIVO, DEFAULT_GRILLA)
	greedo = Greedo() ; dyno = Dyno()
	VistaJuego.titulo()
	jugar(archivo, greedo, args.no_input)
	VistaJuego.imprimirSeparacion()
	jugar(archivo, dyno, args.no_input)
	VistaJuego.imprimirGanador(greedo, dyno)

if __name__ == '__main__':
	try: main()
	except KeyboardInterrupt: pass # Exit smoothly
