from Jugador import Jugador
from copy import deepcopy


class Greedo(Jugador):
	"""
	Greedo Smart:
		Greedy: De mi conjunto de turnos a jugar, mi subproblema es hacer el mejor turno
		Turno optimo: El que mas barcos mata, y de esos el que mas danio saca

	Ojo!
	Sumatoria turnos optimos != Juego optimo
	"""

	def __init__(self):
		super().__init__('Greedo')

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		# Deepcopy hace copias de todos los objetos dentro del objeto, entonces puedo sacarles vida a mis barcos sin molestar a la partida original, de la cual no puedo ni debo tocar nada
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []

		while not simulacion.terminada():
			targets = self.elegirTargetsDelTurno(simulacion)
			simulacion.setTargetDelTurno(targets)
			simulacion.jugarTurno()
			targetsTotales.append(targets)

		return targetsTotales
	
	def elegirTargetsDelTurno(self, partida):
		"""Esta funcion y metodologia es valida porque greedy me pide lo mejor para mi subproblema actual, sin pensar en el resto
		Puedo iterar mis turnos y elegir para cada turno por separado"""
		barcos, lanzaderas = partida.getBarcosVivos(), partida.getCantidadLanzaderas()

		# Diccionario de listas de [Tiros suficientes para matarlo en este turno, danio en casilla, vida]
		atributosBarco = {}

		for barco in barcos:
			vida = barco.getVida()
			danio = partida.getDanioCasillero(*barco.getPosicion())
			atributosBarco[barco] = (tirosParaMatarlo(vida, danio), danio, vida, barco.getID())

		targets = []
		for i in range(lanzaderas):
			barcoActual = max(atributosBarco, key=maxSegunTiro(atributosBarco))
			tirosParaMatar, danio, vida, id = atributosBarco[barcoActual]
			if not (lanzaderas - i >= tirosParaMatar):
				barcoActual = max(atributosBarco, key=maxSegunDanio(atributosBarco))
				tirosParaMatar, danio, vida, id = atributosBarco[barcoActual]
			targets.append(barcoActual.getID())
			vida -= danio
			atributosBarco[barcoActual] = tirosParaMatar-1, danio, vida, id
			if vida <=0:
				atributosBarco.pop(barcoActual)
				if not atributosBarco: break
		targets += [None] * (lanzaderas - len(targets))
		return targets


def tirosParaMatarlo(vida, danio):
	if danio==0: danio = 1
	return -(-vida//danio)

def maxSegunTiro(dic):
	return lambda x: (-dic[x][0], dic[x][1], -dic[x][3])

def maxSegunDanio(dic):
	return lambda x: (dic[x][1], -dic[x][3])