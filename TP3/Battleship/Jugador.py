class Jugador():
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre

	def elegirTargetsDeLaPartida(self, partida):
		"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy/simulacion)
		Devuelve todos los turnos a jugar"""
		raise NotImplementedError