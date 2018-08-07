from Partida import Partida
from Barco import Barco

class Juego():
	"""Clase modelo de un Juego, que es un conjunto de partidas.
	Guarda su matriz, barcos y cantidad de lanzaderas ya que estos son los mismos para toda partida"""
	def __init__(self, matriz, barcos, cantidadLanzaderas):
		self.partidas = []
		self.matriz = matriz
		self.barcos = barcos
		self.cantidadLanzaderas = cantidadLanzaderas

	def nuevaPartidaCon(self, jugador, posicionesDefault):
		for b in self.barcos: b.resetVida()
		partida = Partida(self.matriz, self.barcos, self.cantidadLanzaderas, jugador)
		if posicionesDefault: partida.setPosicionesDefault()
		self.partidas.append(partida)
		return partida

	@staticmethod
	def ArchivoToBarcos(archivo):
		vida_barcos = []
		with open(archivo) as f:
			for linea in f:
				linea = linea.split()
				vida = int(linea[0])
				vida_barcos.append(vida)
		barcos = []
		for vida in vida_barcos:
			barcos.append(Barco(vida))
		return barcos

	@staticmethod
	def ArchivoToMatriz(archivo):
		matriz = []
		with open(archivo) as f:
			for linea in f:
				linea = linea.split()
				linea = linea[1:] # El primer valor es un barco
				linea = [int(x) for x in linea]
				matriz.append(linea)
		return matriz
