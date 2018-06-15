class Jugador():
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre

	def elegirTargetsDeLaPartida(self, partida):
		"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy/simulacion)
		Devuelve una lista de filas de barcos a los que ataca cada lanzadera"""
		pass
