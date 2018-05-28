class Vertice:


	def __init__(self, numero):
		self.numero = numero
		self.adyacentes = []
	
	
	def __str__(self):
		return str(self.numero)
	
		
	def __repr__(self):
		return self.__str__()
	
	
	def __equals__(self, otroVertice):
		return self.numero == otroVertice.obtenerNumero()
	
	
	def agregarAdyacente(self, vertice):
		self.adyacentes.append(vertice)


	def obtenerAdyacentes(self):
		return self.adyacentes


	def obtenerNumero(self):
		return self.numero
