import os
import CrearGrilla
from Partida import Partida
from VistaPartida import VistaPartida
from Juego import Juego
from VistaJuego import VistaJuego
from Greedo import Greedo
from Dyno import Dyno
import argparse

# Filas, Columnas, Rango de Vida barco, maximo danio de celda
# De querer usar otra grilla, se recomienda crearla con CrearGrilla.py y pasarle los parametros a ese archivo
DEFAULT_GRILLA = [5, 10, (500, 1000), 300]

DEFAULT_LANZADERAS = 2 # Se puede pisar con argumentos al ejecutar el programa
ARCHIVO = 'grilla.coords'


def jugar(partida, vista):
	vista.start()
	partida.elegirTodosLosTargets()
	while not partida.terminada():
		targets = partida.elegirTargets()
		vista.informacionTurno()
		vista.imprimirMapa()
		partida.jugarTurno(targets)
	vista.informacionTurno()
	vista.imprimirMapa()
	vista.end()


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-y', '--no-input', help='Deshabilitar el input del usuario', action='store_true')
	parser.add_argument('-o', '--overwrite', help='Sobreescribir el mapa al comenzar la ejecución', action='store_true')
	parser.add_argument('-l', '--lanzaderas', help='Elegir la cantidad de lanzaderas a usar', type=int, action='store', default=DEFAULT_LANZADERAS)
	args = parser.parse_args()

	archivo = ARCHIVO

	if CrearGrilla.archivoNoExiste(archivo) or args.overwrite:
		archivo = CrearGrilla.crearArchivo(ARCHIVO, DEFAULT_GRILLA)

	matrizTablero = Juego.ArchivoToMatriz(archivo)
	barcos = Juego.ArchivoToBarcos(archivo)
	cantidadLanzaderas = args.lanzaderas

	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
	vistaJuego = VistaJuego(juego, args.no_input)
	vistaJuego.titulo()

	jugadores = [Greedo(), Dyno()]
	for i,j in enumerate(jugadores):
		juego.agregarJugador(j)
		partida = juego.nuevaPartidaCon(j)
		vistaPartida = vistaJuego.nuevaVistaPartida(partida)
		jugar(partida, vistaPartida)
		if i != len(jugadores)-1: vistaJuego.cambioDeTurno()
	vistaJuego.imprimirGanador()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass  # Exit smoothly
