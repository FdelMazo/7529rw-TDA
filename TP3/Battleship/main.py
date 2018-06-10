import CrearGrilla
from Juego import Juego
from VistaJuego import VistaJuego
from Greedo import Greedo
from Dyno import Dyno
import argparse

# Filas, Columnas, Rango de Vida barco, maximo danio de celda
# De querer usar otra grilla, se recomienda crearla con CrearGrilla.py y pasarle los parametros a ese archivo
DEFAULT_GRILLA = [5, 10, (500, 1000), 300]

DEFAULT_LANZADERAS = 2
DEFAULT_ARCHIVO = 'grilla.coords'


def jugar(partida, vista,jugador):
	vista.start()
	todosLosTargets = jugador.elegirTargetsDeLaPartida(partida)
	for target in todosLosTargets:
		partida.setTargetDelTurno(target)
		vista.informacionTurno()
		vista.imprimirMapa()
		partida.jugarTurno()
	vista.informacionTurno()
	vista.imprimirMapa()
	vista.end()

	if not partida.terminada():
		# Nunca se debería entrar a este if.
		raise RuntimeError("El jugador NO gano el juego. No fue deterministico su comportamiento.")



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-y', '--no-input', help='Deshabilitar el input del usuario', action='store_true')
	parser.add_argument('-o', '--sobreescribir', help='Sobreescribir el mapa al comenzar la ejecución', action='store_true')
	parser.add_argument('-l', '--lanzaderas', help='Elegir la cantidad de lanzaderas a usar', type=int, action='store', default=DEFAULT_LANZADERAS)
	parser.add_argument('-f', '--archivo', help='Elegir el archivo de mapa a usar', action='store', default=DEFAULT_ARCHIVO)
	args = parser.parse_args()

	archivo = args.archivo

	if CrearGrilla.archivoNoExiste(archivo) or args.sobreescribir:
		archivo = CrearGrilla.crearArchivo(args.archivo, DEFAULT_GRILLA)

	try:
		CrearGrilla.verificarGrilla(archivo)
	except IOError as e:
		print(e)
		return

	matrizTablero = Juego.ArchivoToMatriz(archivo)
	barcos = Juego.ArchivoToBarcos(archivo)
	cantidadLanzaderas = args.lanzaderas

	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
	vistaJuego = VistaJuego(juego, args.no_input)
	vistaJuego.titulo()

	jugadores = [Greedo()]
	for i,jugador in enumerate(jugadores):
		juego.agregarJugador(jugador)
		partida = juego.nuevaPartidaCon(jugador)
		vistaPartida = vistaJuego.nuevaVistaPartida(partida)
		jugar(partida, vistaPartida, jugador)
		if i != len(jugadores)-1: vistaJuego.cambioDeTurno()
	vistaJuego.imprimirGanador()
	return

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass  # Exit smoothly
