from Jugador import Jugador
from copy import deepcopy
import itertools

class Brutus(Jugador):
	"""
	Brutus:
		Greedy: De mi conjunto de turnos a jugar, mi subproblema es hacer el mejor turno
		Fuerza Bruta: Saco todas las posibles combinaciones de mi turno y elejo el optimo de eso.
		Turno optimo: El que mas mata, y despues el que mas danio saca

	Ojo!
	Sumatoria turnos optimos != Juego optimo
	"""

	def __init__(self):
		super().__init__('Brutus')

	def todasLasCombinacionesPosibles(self, barcos, cantidadTiros):
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

	def elegirTargetDelTurno(self, partida):
		barcos, lanzaderas = partida.getBarcos(), partida.getCantidadLanzaderas()
		danios = [partida.getDanioCasillero(*b.getPosicion()) for b in barcos]
		combinacionesPosibles = self.todasLasCombinacionesPosibles(barcos,lanzaderas)
		mejorTurno = self.turnoOptimo(combinacionesPosibles, barcos, danios)
		return mejorTurno

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []

		while not simulacion.terminada():
			targets = self.elegirTargetDelTurno(simulacion)
			simulacion.setTargetDelTurno(targets)
			simulacion.jugarTurno()
			targetsTotales.append(targets)

		return targetsTotales

	def turnoOptimo(self,listaTargets, barcos, danios):
		"""Para el subproblema de cual es el mejor turno posible, es decir, el que menos puntos haga pasar y mas danio haga es:
			El turno que mas barcos derribe
			De esos, el que menos tiros gaste en el barco
			De esos, el que mas danio produzca"""
		"""Recibe una lista con todas las combinaciones posibles de disparos (por ejemplo, un disparo al tercer barco con solo dos lanzaderas es [3,3]
			Los simula, y agarra sus atributos (cantidad muertes, cuanto danio hizo, cuanto le cuesta matar
			Los ordena establemente con los criterios
			Devuelve el mejor"""
		atributos = [] #Lista de tuplas de Muertos, SumVida, SumatoriaTirosPaMatar
		for posibilidad in listaTargets:
			turno = self.simularTurno(barcos, danios, posibilidad)
			muertos = []
			sumatoriaTirosParaMatar = 0
			for i,b in enumerate(turno):
				if b <= 0:
					muertos.append(b)
					sumatoriaTirosParaMatar = posibilidad.count(i)
			sumatoriaVidas = sum([b for b in turno if b>0])
			atributos.append((sumatoriaVidas,len(muertos), sumatoriaTirosParaMatar))

		atributosOrdenados = sorted(atributos, key=lambda x:(-x[1],x[2],x[0]))
		indice = atributos.index(atributosOrdenados[0])
		return listaTargets[indice]


	def simularTurno(self, barcos, danios, target):
		"""Recibe una lista de barcos y a quienes atacar y devuelve como quedarian sus vidas"""
		vidasBarcos = [b.getVida() for b in barcos]
		for n in target:
			vidasBarcos[n] -= danios[n]
		return vidasBarcos
