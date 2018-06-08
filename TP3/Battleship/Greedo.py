from Jugador import Jugador
from copy import copy,deepcopy


class Greedo(Jugador):
	def __init__(self):
		super().__init__('Greedo')

	def elegirTargets(self, juego):
		danioSegunBarco = {}
		for barco in juego.getBarcosVivos():
			x, y = barco.getPosicion()
			danioSegunBarco[barco] = juego.getDanioCasillero(x, y)
		barcosOrdenados = sorted(danioSegunBarco.items(), key=lambda x: x[1])
		barcosDisponibles = len(barcosOrdenados)
		barcoActual = barcosOrdenados[barcosDisponibles - 1]
		targets = []
		for i in range(juego.getCantidadLanzaderas()):
			barco, danio = barcoActual
			dummyVida = barco.getVida()
			dummyVida -= danio
			targets.append(barco)
			if dummyVida <= 0:
				barcosDisponibles -= 1
				if barcosDisponibles == 0:
					break
				barcoActual = barcosOrdenados[barcosDisponibles-1]
		targets += [None] * (juego.getCantidadLanzaderas() - len(targets))
		return [t.getPosicion()[1] if t else None for t in targets ]

	def elegirTodosLosTargets(self, partidaOriginal):
		"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy/simulacion)
		Devuelve una lista de filas de barcos a los que ataca cada lanzadera"""
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []

		while not simulacion.terminada():
			targets = self.elegirTargets(simulacion)
			simulacion.jugarTurno(targets)
			targetsTotales.append(targets)

		return targetsTotales