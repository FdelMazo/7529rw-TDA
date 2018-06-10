from Jugador import Jugador
from copy import deepcopy


class GreedoNaive(Jugador):
	"""
	Greedo Naive (AKA: Greedy del Greedy):
		Greedy: De mi conjunto de turnos a jugar, hago el mejor turno posible
		Greedy del Greedy: De mi turno a jugar, mi mejor turno es donde las lanzaderas hagan el mayor danio posible

	Agarro el juego entero y lo simulo.
	Como necesito el mejor turno (con mis condiciones de que el mejor == el que mas danio hace), puedo iterar.
	Nunca me importa el resto de los turnos. Solo el actual.

	for turno in turnos:
		for lanzadera in lanzaderas:
			hago el mayor danio posible
	"""

	def __init__(self):
		super().__init__('Greedo Naive')

	def elegirTargetDelTurno(self, partida):
		barcos, lanzaderas = partida.getBarcosVivos(), partida.getCantidadLanzaderas()
		danioSegunBarco = []
		for barco in reversed(barcos):
			x, y = barco.getPosicion()
			danioSegunBarco.append((barco, partida.getDanioCasillero(x, y)))
		danioSegunBarco.sort(key=lambda x: x[1])
		barcoActual = danioSegunBarco[-1]
		vidaActual = barcoActual[0].getVida()
		targets = []
		for i in range(lanzaderas):
			barco, danio = barcoActual
			vidaActual -= danio
			targets.append(barco.getID())
			if vidaActual <=0:
				danioSegunBarco.pop()
				if not danioSegunBarco: break
				barcoActual = danioSegunBarco[-1]
				vidaActual = barcoActual[0].getVida()
		targets += [None] * (lanzaderas - len(targets))
		return targets

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []

		while not simulacion.terminada():
			targets = self.elegirTargetDelTurno(simulacion)
			simulacion.setTargetDelTurno(targets)
			simulacion.jugarTurno()
			targetsTotales.append(targets)

		return targetsTotales