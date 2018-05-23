class Vertice:


	def __init__(self, numero):
		self.numero = numero
		self.adyacentes = {}
	
	
	def __str__(self):
		return str(self.numero)
				
	
	def __equals__(self, otroVertice):
		return self.numero == otroVertice.numero
	
	
	def agregarAdyacente(self, vertice):
		self.adyacentes[ len(self.adyacentes) ] = vertice


	def obtenerAdyacentes(self):
		return list(self.adyacentes.values())


	def obtenerNumero(self):
		return self.numero
