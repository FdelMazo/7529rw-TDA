from Jugador import Jugador
from copy import deepcopy


class Dyno(Jugador):
	"""
	Dyno dyno
	"""

	def __init__(self):
		super().__init__('Dyno')

	def elegirTargetDelTurno(self, partida):
		barcos, lanzaderas = partida.getBarcos(), partida.getCantidadLanzaderas()
		danios = [partida.getDanioCasillero(*b.getPosicion()) for b in barcos]
		combinacionesPosibles = self.todasLasCombinacionesPosibles(barcos,lanzaderas)
		mejorTurno = self.turnoOptimo(combinacionesPosibles, barcos, danios)
		return mejorTurno

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []
		matriz = simulacion.getMatriz()

		vuelta, ultimaColumna = max([self.turnoDondeMuere(b, matriz) for b in simulacion.getBarcos()]	)
		cantidadColumnas = len(simulacion.getMatriz()[0])
		cantidadBarcos = len(simulacion.getBarcos())


		cotaTotal = vuelta*cantidadColumnas*cantidadBarcos
		#print(vuelta, cantidadColumnas,cotaTotal)

		while not simulacion.terminada():
			targets = self.elegirTargetDelTurno(simulacion)
			simulacion.setTargetDelTurno(targets)
			simulacion.jugarTurno()
			targetsTotales.append(targets)

		return targetsTotales

# if __name__=='__main__':
# 	from Juego import Juego
# 	from Partida import Partida
#
# 	archivo = 'grilla.coords'
# 	matrizTablero = Juego.ArchivoToMatriz(archivo)
# 	barcos = Juego.ArchivoToBarcos(archivo)
# 	cantidadLanzaderas = 3
#
# 	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
# 	jugador = Dyno()
# 	partida = Partida(matrizTablero, barcos, cantidadLanzaderas, jugador)
# 	partida.setPosicionesIniciales()
# 	jugador.elegirTargetsDeLaPartida(partida)
