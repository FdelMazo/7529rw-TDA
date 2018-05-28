class Vertice:


	def __init__(self, numero, info = None):
		self.numero = numero
		self.adyacentes = []
		self.info = info
	
	
	def __str__(self):
		return str(self.numero)

	
	def __repr__(self):
		return self.__str__()


	def agregarAdyacente(self, vertice):
		self.adyacentes.append(vertice)


	def obtenerAdyacentes(self):
		return self.adyacentes


	def obtenerNumero(self):
		return self.numero


	def esIgualA(self, otroVertice):
		return self.numero == otroVertice.obtenerNumero()	
