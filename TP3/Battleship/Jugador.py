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

	def elegirTargetDelTurno(self, juego):
		pass

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		pass
