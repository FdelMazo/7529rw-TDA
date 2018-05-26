class Arista:

	
	def __init__(self, origen, destino, peso):
		self.origen = origen
		self.destino = destino
		self.peso = peso
	
	
	def __str__(self):
		return str(self.origen) + ' -> ' + str(self.destino)


	def __equals__(self, otraArista):
		return ( self.origen == otraArista.obtenerOrigen() and
		self.destino == otraArista.obtenerDestino() and
		self.peso == otraArista.obtenerPeso() )


	def obtenerOrigen(self):
		return self.origen


	def obtenerDestino(self):
		return self.destino


	def obtenerPeso(self):
		return self.peso


	def setPeso(self, nuevoPeso):
		self.peso = nuevoPeso
