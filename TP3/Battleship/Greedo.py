from Jugador import Jugador
from copy import deepcopy


class Greedo(Jugador):
	"""
	Greedo Smart:
		Greedy: De mi conjunto de turnos a jugar, mi subproblema es hacer el mejor turno
		Fuerza Bruta: Saco todas las posibles combinaciones de mi turno y elejo el optimo de eso.
		Turno optimo: El que mas mata, y despues el que mas danio saca

	Dentro del problema del turno (y no del juego), esta solucion es la optima,
		ya que si mi objetivo final es producir la menor cantidad de puntos posibles, con esto los disminiyo a su maximo,
		gracias a que estoy produciendo la mayor cantidad de muertes posibles
		En la decision de generar x muertes en dos turnos iguales, se torna a generar mayor danio posible.

	Ojo!
	Sumatoria turnos optimos != Juego optimo
	"""

	def __init__(self):
		super().__init__('Greedo')

	def elegirTargetDelTurno(self, partida):
		"""Esta funcion y metodologia es valida porque greedy me pide lo mejor para mi subproblema actual, sin pensar en el resto
		Puedo iterar mis turnos y elegir para cada turno por separado"""
		barcos, lanzaderas = partida.getBarcosVivos(), partida.getCantidadLanzaderas()

		# Diccionario de listas de [Tiros suficientes para matarlo en este turno, danio en casilla, vida]
		atributosBarco = {}

		for barco in barcos:
			x, y = barco.getPosicion()
			danio = partida.getDanioCasillero(x, y)
			vida = barco.getVida()
			id = barco.getID()
			tirosParaMatar = lanzaderas+1 # Equivalente a poner en infinito
			for i in range(1,lanzaderas+1):
				if i*danio >=vida:
					tirosParaMatar = i
					break
			atributosBarco[barco] = (tirosParaMatar, danio, barco.getVida(), id)

		def sortPorTiros(dic):
			return lambda x: (-dic[x][0],dic[x][1], -dic[x][3])

		def sortPorDanio(dic):
			return lambda x: (dic[x][1], -dic[x][3])

		targets = []
		for i in range(lanzaderas):
			barcoActual = max(atributosBarco, key=sortPorTiros(atributosBarco))
			tirosParaMatar, danio, vida, id = atributosBarco[barcoActual]
			if not (lanzaderas - i >= tirosParaMatar):
				barcoActual = max(atributosBarco, key=sortPorDanio(atributosBarco))
			targets.append(barcoActual.getID())
			vida -= danio
			atributosBarco[barcoActual] = tirosParaMatar-1, danio, vida, id
			if vida <=0:
				atributosBarco.pop(barcoActual)
				if not atributosBarco: break
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