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

	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
	juego.setJugador(jugador)
	juego.setPosicionesIniciales()
	vista = VistaJuego(juego, no_input)
	vista.start()
	while not juego.terminado():
		juego.jugar()
		vista.informacionAdicional()
		vista.update()
		juego.avanzarTurno()
	vista.informacionAdicional()
	vista.update()
	vista.end()
	return juego.getPuntos()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--no-input',help='Deshabilitar el input del usuario', action = 'store_true')
	args = parser.parse_args()

	archivo = ARCHIVO
	if not os.path.exists(archivo):
		archivo = CrearGrilla.crearArchivo(ARCHIVO, DEFAULT_GRILLA)
	greedo = Greedo() ; dyno = Dyno()
	puntosGreedo = jugar(archivo, greedo, args.no_input)
	VistaJuego.imprimirSeparacion()
	puntosDyno = jugar(archivo, dyno, args.no_input)
	VistaJuego.imprimirGanador(puntosGreedo, puntosDyno)