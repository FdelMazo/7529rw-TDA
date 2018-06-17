import CrearGrilla
from Juego import Juego
from VistaJuego import VistaJuego
from Greedo import Greedo
from Dyno import Dyno
import BandoA
import argparse

# Filas, Columnas, Rango de Vida barco, maximo danio de celda
# De querer usar otra grilla, crearla con CrearGrilla.py y pasarle los parametros a ese archivo
DEFAULT_GRILLA = [5, 10, (500, 1000), 300]
DEFAULT_LANZADERAS = 3
DEFAULT_ARCHIVO = 'grilla.coords'

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-y', '--no-input', help='Deshabilitar el input del usuario', action='store_true')
	parser.add_argument('-o', '--sobreescribir', help='Sobreescribir el mapa al comenzar la ejecución', action='store_true')
	parser.add_argument('-l', '--lanzaderas', help='Elegir la cantidad de lanzaderas a usar', type=int, action='store', default=DEFAULT_LANZADERAS)
	parser.add_argument('-f', '--archivo', help='Elegir el archivo de mapa a usar', action='store', default=DEFAULT_ARCHIVO)
	parser.add_argument('-p', '--set-posiciones-iniciales', help='Permitir a A setear las posiciones de los barcos', action='store_true')
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
	cantidadLanzaderas = args.lanzaderas or DEFAULT_LANZADERAS #Si usa --lanzaderas 0

	if args.set_posiciones_iniciales:
		BandoA.setPosiciones(matrizTablero, barcos, cantidadLanzaderas)

	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
	vistaJuego = VistaJuego(juego, args.no_input)
	vistaJuego.titulo()
	jugadores = [Greedo(), Dyno()] #Se puede extender la lista para incluir otros jugadores. Ej: [Greedo(), Dyno(), Brutus()]
	for i,jugador in enumerate(jugadores):
		partida = juego.nuevaPartidaCon(jugador, not args.set_posiciones_iniciales)
		vistaPartida = vistaJuego.nuevaVistaPartida(partida)
		jugar(partida, vistaPartida, jugador)
		if i != len(jugadores)-1: vistaJuego.cambioDeTurno()
	vistaJuego.imprimirGanador()
	return

def jugar(partida, vista,jugador):
	vista.start()
	# Es importante que cada jugador reciba toda la partida y devuelva todos los turnos a jugar, NO lo puede hacer turno a turno
	# Los targets de una partida estan implementados como una lista de listas:
	# Cada target es una lista de a que ID de barcos ataca cada lanzadera: [1,2] ataca al barco en la fila 1 con una lanzadera y al barco en la fila 2 con la segunda
	# [ [1,2], [1, None], [2,2] ] Es una partida de 3 turnos y dos lanzaderas
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
		# Nunca nunca nunca se debería entrar a este if.
		raise RuntimeError("El jugador NO gano el juego.")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass  # Exit smoothly


