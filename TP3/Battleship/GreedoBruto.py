from Jugador import Jugador
from copy import deepcopy
import itertools


def listaOptima(listas):
	# Medio polimorfica la funcion... Si recibe una lista de listas de listas, la hace lista de listas
	if isinstance(listas[0], list) and isinstance(listas[0][0], list):
		listas = [item for sublist in listas for item in sublist]

	listasSinDup = []
	for l in listas:
		if l not in listasSinDup: listasSinDup.append(l)
	listas = listasSinDup

	atributos = []
	for lista in listas:
		sumatoria, cantidadDerribados = sum([a for a in lista if a > 0]), len([a for a in lista if a <= 0])
		atributos.append((sumatoria, cantidadDerribados))
	opt = 0
	for i in range(len(listas)):
		if atributos[i][1] > atributos[opt][1]:
			opt = i
		elif atributos[i][1] == atributos[opt][1] and atributos[i][0] < atributos[opt][0]:
			opt = i

	return listas[opt]

def todasLasCombinacionesPosibles(barcos, cantidadTiros):
	"""Recibe la cantidad de barcos y la cantidad de tiros posibles en el turno
	Devuelve una lista de listas con todas las combinaciones posibles"""
	barcos = [b.getID() for b in barcos]

	# Algun dia aprendere combinatoria....
	# Hacer todas las combinaciones posibles con itertools y agregarlas ordenadas a un set para que no se repitan
	combinacionesConRepeticiones = itertools.product(barcos, repeat=cantidadTiros)

	combinacionesSinRepeticiones = set()
	for c in combinacionesConRepeticiones:
		combinacionesSinRepeticiones.add(tuple(sorted(c)))

	listaDeListas = []
	for c in combinacionesSinRepeticiones:
		listaDeListas.append(list(c))

	return listaDeListas

def simularTurno(barcos, danios, target):
	"""Recibe una lista de barcos y a quienes atacar y devuelve como quedarian sus vidas"""
	vidasBarcos = [b.getVida() for b in barcos]
	for n in target:
		vidasBarcos[n] -= danios[n]
	return vidasBarcos

class GreedoBruto(Jugador):
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
	"""

	def __init__(self):
		super().__init__('Greedo Bruto')

	def elegirTargetDelTurno(self, partida):
		barcos, lanzaderas = partida.getBarcos(), partida.getCantidadLanzaderas()
		danios = [partida.getDanioCasillero(*b.getPosicion()) for b in barcos]

		combinacionesPosibles = todasLasCombinacionesPosibles(barcos,lanzaderas)
		simulaciones = []
		for posibilidad in combinacionesPosibles:
			simulaciones.append(simularTurno(barcos, danios, posibilidad))

		mejorSimulacion = listaOptima(simulaciones)

		mejorPosibilidad = combinacionesPosibles[simulaciones.index(mejorSimulacion)]
		return mejorPosibilidad

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy/simulacion)
		Devuelve una lista de filas de barcos a los que ataca cada lanzadera"""
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []

		while not simulacion.terminada():
			targets = self.elegirTargetDelTurno(simulacion)
			simulacion.setTargetDelTurno(targets)
			simulacion.jugarTurno()
			targetsTotales.append(targets)

		return targetsTotales