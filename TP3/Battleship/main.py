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

DEFAULT_LANZADERAS = 1
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
	cantidadLanzaderas = args.lanzaderas

	if args.set_posiciones_iniciales:
		BandoA.setPosiciones(matrizTablero, barcos, cantidadLanzaderas)

	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
	vistaJuego = VistaJuego(juego, args.no_input)
	vistaJuego.titulo()
	jugadores = [Greedo(), Dyno()]
	for i,jugador in enumerate(jugadores):
		juego.agregarJugador(jugador)
		partida = juego.nuevaPartidaCon(jugador, not args.set_posiciones_iniciales)
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
