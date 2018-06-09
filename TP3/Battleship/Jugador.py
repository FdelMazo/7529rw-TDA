import itertools


class Jugador():
	def __init__(self, nombre):
		self.nombre = nombre
		self.puntos = 0

	def __str__(self):
		return self.nombre

	def getPuntos(self):
		return self.puntos

	def addPuntos(self, puntos):
		self.puntos += puntos

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		pass

	def turnoDondeMuere(self, barco, matriz):
		"""Devuelve la primera columna en el que se le puede ganar a un barco con la tupla (NroVuelta, Columna)
		Ojo, ambos indices comienzan en 1 en vez de en 0, porque se refieren a vueltas y a columnas (no turnos)"""
		numFila = barco.getID()
		fila = matriz[numFila]
		objetivo = barco.getVida()

		vuelta = 1
		while objetivo > 0:
			for i,elem in enumerate(fila,1):
				objetivo -= elem
				if objetivo <= 0: break
			if objetivo<=0: break
			vuelta+=1
		return (vuelta, i)

	def turnoOptimo(self,listaTargets, barcos, danios):
		"""Para el subproblema de cual es el mejor turno posible, es decir, el que menos puntos haga pasar y mas danio haga es:
			El turno que mas barcos derribe
			De esos, el que menos tiros gaste en el barco
			De esos, el que mas danio produzca"""
		"""Recibe una lista con todas las combinaciones posibles de disparos (por ejemplo, un disparo al tercer barco con solo dos lanzaderas es [3,3]
			Los simula, y agarra sus atributos (cantidad muertes, cuanto danio hizo, cuanto le cuesta matar
			Los ordena establemente con los criterios
			Devuelve el mejor"""
		atributos = [] #Lista de tuplas de Targets, Muertos, SumVida, SumatoriaTirosPaMatar
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

	def todasLasCombinacionesPosibles(self, barcos, cantidadTiros):
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

	def simularTurno(self, barcos, danios, target):
		"""Recibe una lista de barcos y a quienes atacar y devuelve como quedarian sus vidas"""
		vidasBarcos = [b.getVida() for b in barcos]
		for n in target:
			vidasBarcos[n] -= danios[n]
		return vidasBarcos
