from Jugador import Jugador
from copy import deepcopy


class Greedo(Jugador):
	"""
	Greedy Naive (AKA: Greedy del Greedy):
		Greedy: De mi conjunto de turnos a jugar, mi subproblema es hacer el turno con mas danio posible
		Greedy del Greedy: De mi turno a jugar, mi subproblema es que la lanzadera haga el mayor danio posible

	Agarro el juego entero y lo simulo.
	Como necesito ganar el turno, puedo iterar. Nunca me importa el resto de los turnos. Solo el actual

	for turno in turnos:
		for lanzadera in lanzaderas:
			hago el mayor danio posible
	"""

	def __init__(self):
		super().__init__('Greedo')

	def elegirTargets(self, partida):
		barcos, lanzaderas = partida.getBarcosVivos(), partida.getCantidadLanzaderas()
		danioSegunBarco = {}
		for barco in barcos:
			x, y = barco.getPosicion()
			danioSegunBarco[barco] = partida.getDanioCasillero(x, y)
		barcosOrdenados = sorted(danioSegunBarco.items(), key=lambda x: x[1])
		barcosDisponibles = len(barcosOrdenados)
		barcoActual = barcosOrdenados[barcosDisponibles - 1]
		targets = []
		for i in range(lanzaderas):
			barco, danio = barcoActual
			dummyVida = barco.getVida() - danio
			targets.append(barco.getID())
			if dummyVida <= 0:
				barcosDisponibles -= 1
				if barcosDisponibles == 0:
					break
				barcoActual = barcosOrdenados[barcosDisponibles-1]
		targets += [None] * (lanzaderas - len(targets))
		return targets

	def elegirTodosLosTargets(self, partidaOriginal):
		"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy/simulacion)
		Devuelve una lista de filas de barcos a los que ataca cada lanzadera"""
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []

		while not simulacion.terminada():
			targets = self.elegirTargets(simulacion)
			simulacion.setTargets(targets)
			simulacion.jugarTurno()
			targetsTotales.append(targets)

		return targetsTotales