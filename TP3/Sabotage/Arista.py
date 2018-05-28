class Arista:

	
	def __init__(self, origen, destino, peso, identificador = None):
		self.origen = origen
		self.destino = destino
		self.peso = peso
		self.identificador = identificador
	
	
	def __str__(self):
		return ('(' + str(self.origen) + ',' + str(self.destino) + 
		') [' +  str(self.peso) + ']\n')
	

	def __repr__(self):
		return self.__str__()	

	def obtenerOrigen(self):
		return self.origen


	def obtenerDestino(self):
		return self.destino


	def obtenerPeso(self):
		return self.peso


	def setPeso(self, nuevoPeso):
		self.peso = nuevoPeso


	def obtenerId(self):
		return self.identificador


	def setId(self, identificador):
		self.identificador = identificador


	def esIgualA(self, otraArista):
		return ( 
		self.origen.obtenerNumero() == otraArista.obtenerOrigen().obtenerNumero() 
		and self.destino.obtenerNumero() == otraArista.obtenerDestino().obtenerNumero() 
		and self.peso == otraArista.obtenerPeso() 
		)
