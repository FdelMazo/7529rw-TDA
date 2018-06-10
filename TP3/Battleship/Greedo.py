from Jugador import Jugador
from copy import deepcopy


class Greedo(Jugador):
	"""
	Greedo Smart:
		Greedy: De mi conjunto de turnos a jugar, tengo que hacer siempre el mejor turno (localmente hago lo mejor, no me importa el resto)
		En vez de mi mejor turno ser el que mas danio saca (Naive), ahora es el que mas mata, y luego el que mas saca.

		Por ejemplo, teniendo 3 barcos y 2 lanzaderas:
			300hp \ 60
			200hp \ 50
			100hp \ 50

		La version Naive diria que el mejor target es el [0,0] (disparar dos veces al barco de 300hp), porque es el que mas danio produce
		La version Smart diria que el mejor target es el [2,2] (disparar dos veces al barco de 100hp), porque es el que mas muertes produce, sin importar el danio

	Agarro el juego entero y lo simulo.
	Como necesito el mejor turno (con mis condiciones de que el mejor == el que mas danio hace), puedo iterar.
	Nunca me importa el resto de los turnos. Solo el actual.

	for turno in turnos:



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
		"""Esta funcion y metodologia es valida porque greedy me pide lo mejor para mi subproblema, sin pensar en el resto
		Puedo iterar mis turnos y elegir para cada turno por separado"""
		barcos, lanzaderas = partida.getBarcosVivos(), partida.getCantidadLanzaderas()
		atributosBarco = {} #Lista de listas de (Barco, Danio en su casillero, Tiros para matarlo en este turno)

		for barco in reversed(barcos): #reversed para que sea estable el ordenamiento y si tiene dos barcos con la misma vida elija en orden
			x, y = barco.getPosicion()
			danio = partida.getDanioCasillero(x, y)
			vida = barco.getVida()
			tirosParaMatar = lanzaderas+2 # Equivalente a poner en infinito
			for i in range(1,lanzaderas+1):
				if i*danio >=vida:
					tirosParaMatar = i
					break
			atributosBarco[barco] = (tirosParaMatar, danio, barco.getVida())

		def sortPorTiros(dic):
			"""Ordena tuplas por su primer valor en orden descendente, y luego por su segundo valor en orden ascendente"""
			return lambda x: (-dic[x][0],dic[x][1])

		def sortPorDanio(dic):
			"""Ordena tuplas por su segundo valor en orden ascendente"""
			return lambda x: (dic[x][1])

		targets = []
		for i in range(lanzaderas):
			barcoActual = max(atributosBarco, key=sortPorTiros(atributosBarco))
			tirosParaMatar, danio, vida = atributosBarco[barcoActual]
			if lanzaderas - (i+1) > tirosParaMatar:
				barcoActual = max(atributosBarco, key=sortPorDanio(atributosBarco))
			targets.append(barcoActual.getID())
			vida -= danio
			atributosBarco[barcoActual] = tirosParaMatar, danio, vida
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