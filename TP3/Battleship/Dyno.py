from Jugador import Jugador
from copy import deepcopy


class Dyno(Jugador):
	"""
	Greedy Bruto (AKA: Greedy Inteligente, pero se llama Bruto porque usa un poco de fuerza bruta):
		Greedy: De mi conjunto de turnos a jugar, mi subproblema es hacer el mejor turno
		En vez de mi mejor turno ser el que mas danio saca (Naive), ahora es el que mas mata, y luego el que mas saca.
		Entonces, tengo que sacar todas las posibles combinaciones de mi turno (fuerza bruta) y elegir el optimo de eso.

		Por ejemplo, teniendo 3 barcos y 2 lanzaderas:
			300hp \ 60
			200hp \ 50
			100hp \ 50

		La version Naif diria que el mejor target es el [0,0] (disparar dos veces al barco de 300hp),
			porque es el que mas danio produce
		La version Smart/Bruta diria que el mejor target es el [2,2] (disparar dos veces al barco de 100hp),
			porque es el que mas muertes produce, sin importar el danio

	Agarro el juego entero y lo simulo.
	Como necesito el turno optimo, puedo iterar mi cantidad de turnos. Nunca me importa el resto de los turnos. Solo el actual

	for turno in turnos:
		for lanzadera in lanzaderas:
			hago el mayor danio posible


	Dentro del problema del turno (y no del juego), esta solucion es la optima,
		ya que si mi objetivo final es producir la menor cantidad de puntos posibles, con esto los disminiyo a su maximo,
		gracias a que estoy produciendo la mayor cantidad de muertes posibles
		En la decision de generar x muertes en dos turnos iguales, se torna a generar mayor danio posible.

	Ojo!
	Sumatoria turnos optimos != Juego optimo
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
		"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy/simulacion)
		Devuelve una lista de filas de barcos a los que ataca cada lanzadera"""
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []
		matriz = simulacion.getMatriz()

		vuelta, ultimaColumna = max([self.turnoDondeMuere(b, matriz) for b in simulacion.getBarcos()]	)
		cantidadColumnas = len(simulacion.getMatriz()[0])
		cantidadBarcos = len(simulacion.getBarcos())


		cotaTotal = vuelta*cantidadColumnas*cantidadBarcos
		print(vuelta, cantidadColumnas,cotaTotal)

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
