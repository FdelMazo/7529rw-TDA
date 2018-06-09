from Jugador import Jugador
from copy import deepcopy


class Greedo(Jugador):
	"""
	Greedy Naive (AKA: Greedy del Greedy):
		Greedy: De mi conjunto de turnos a jugar, mi subproblema es hacer el turno con mas danio posible
		Greedy del Greedy: De mi turno a jugar, mi subproblema es que la lanzadera haga el mayor danio posible

	Agarro el juego entero y lo simulo.
	Como necesito el mejor turno (con mis condiciones de que el mejor == el que mas danio hace), puedo iterar. Nunca me importa el resto de los turnos. Solo el actual

	for turno in turnos:
		for lanzadera in lanzaderas:
			hago el mayor danio posible
	"""

	def __init__(self):
		super().__init__('Greedo')

	def elegirTargetDelTurno(self, partida):
		"""Esta funcion y metodologia es valida porque greedy me pide lo mejor para mi subproblema, sin pensar en el resto
		Puedo iterar mis turnos y elegir para cada turno por separado"""
		barcos, lanzaderas = partida.getBarcosVivos(), partida.getCantidadLanzaderas()
		danioSegunBarco = []
		for barco in reversed(barcos):
			x, y = barco.getPosicion()
			danioSegunBarco.append((barco, partida.getDanioCasillero(x, y)))
		barcosOrdenados = sorted(danioSegunBarco, key=lambda x: x[1])
		barcoActual = barcosOrdenados[-1]
		targets = []
		for i in range(lanzaderas):
			barco, danio = barcoActual
			dummyVida = barco.getVida() - danio
			targets.append(barco.getID())
			if dummyVida <= 0:
				barcosOrdenados.pop()
				if not barcosOrdenados: break
				barcoActual = barcosOrdenados[-1]
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