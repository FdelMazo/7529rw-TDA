class Arista:

	
	def __init__(self, origen, destino, peso, flujo = 0):
		self.origen = origen
		self.destino = destino
		self.peso = peso
		self.flujo = flujo
	
	
	def __str__(self):
		return str(self.origen) + ' -> ' + str(self.destino)


	def esDeRegresion(self):
		return False
		

	def obtenerOrigen(self):
		return self.origen


	def obtenerDestino(self):
		return self.destino


	def obtenerPeso(self):
		return self.peso


	def setPeso(self, nuevoPeso):
		self.peso = nuevoPeso
