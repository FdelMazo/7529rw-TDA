class Partida():
	def __init__(self, matriz, barcos, cantidadLanzaderas, jugador):
		self.matriz = matriz
		self.barcos = barcos
		self.cantidadLanzaderas = cantidadLanzaderas
		self.turno = 0
		self.jugador = jugador
		self.targets = []
		self.targetsActuales = [None] * self.cantidadLanzaderas

	def terminada(self):
		return not self.getBarcosVivos()

	def setPosicionesIniciales(self):
		for i, barco in enumerate(self.barcos):
			barco.setPosicion(0,i)

	def avanzarBarcos(self):
		for barco in self.barcos:
			x, y = barco.getPosicion()
			if x == len(self.matriz[y]) - 1:
				barco.setPosicion(0,y)
			else:
				barco.setPosicion(x + 1, y)

	def elegirTodosLosTargets(self):
		self.targets = self.jugador.elegirTodosLosTargets(self)

	def elegirTargets(self):
		self.targetsActuales = self.targets[self.turno]
		return self.targetsActuales

	def jugarTurno(self,targets):
		self.jugador.addPuntos(len(self.getBarcosVivos()))
		for t in targets:
			if t!=None: self.barcos[t].recibirDanio(self.getDanioCasillero(*self.barcos[t].getPosicion()))
		self.avanzarBarcos()
		self.turno += 1

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