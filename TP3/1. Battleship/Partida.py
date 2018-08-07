class Partida():
	"""Clase responsable de la partida de cada jugador, sin idea de el resto de las partidas"""
	def __init__(self, matriz, barcos, cantidadLanzaderas, jugador):
		self.matriz = matriz
		self.barcos = barcos
		self.cantidadLanzaderas = cantidadLanzaderas
		self.turno = 0
		self.puntos = 0
		self.jugador = jugador
		self.targetDelTurno = [None] * self.cantidadLanzaderas

	def __str__(self):
		return "Partida de {} - Puntos del bando A: {} - Turno: {}".format(self.jugador, self.puntos, self.turno)

	def terminada(self):
		return not self.getBarcosVivos()

	def setPosicionesDefault(self):
		for i, barco in enumerate(self.barcos):
			barco.setPosicion(0,i)

	def avanzarBarcos(self):
		for barco in self.barcos:
			x, y = barco.getPosicion()
			if x == len(self.matriz[y]) - 1:
				barco.setPosicion(0,y)
			else:
				barco.setPosicion(x + 1, y)

	def setTargetDelTurno(self, targets):
		self.targetDelTurno = targets

	def jugarTurno(self):
		self.puntos += len(self.getBarcosVivos())
		if self.targetDelTurno:
			for t in self.targetDelTurno:
				# Cabe aclarar (aca o en otro lado del codigo) que se esta lleno de !=None
				# Esto es porque un target puede ser el barco 0, y en python evalua a falso (entonces no se puede hacer if not t)
				if t!=None: self.barcos[t].recibirDanio(self.getDanioCasillero(*self.barcos[t].getPosicion()))
		self.avanzarBarcos()
		self.turno += 1

	def getPuntos(self):
		return self.puntos

	def getBarcosVivos(self):
		return [b for b in self.barcos if not b.estaDerribado()]

	def getBarcos(self):
		return self.barcos

	def getMatriz(self):
		return self.matriz

	def getDanioCasillero(self, x, y):
		return self.matriz[y][x]

	def getCantidadLanzaderas(self):
		return self.cantidadLanzaderas

	def getJugador(self):
		return self.jugador