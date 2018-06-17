class Vertice:


	def __init__(self, numero, info = None):
		self.numero = numero
		self.adyacentes = {}
		self.info = info
	
	
	def __str__(self):
		return str(self.numero)

	
	def __repr__(self):
		return self.__str__()


	def agregarAdyacente(self, vertice):
		try:
			self.adyacentes[vertice].append(vertice)
		except KeyError:
			self.adyacentes[vertice] = [vertice]


	def borrarAdyacente(self, vertice):
		self.adyacentes[vertice].pop()
		if not self.adyacentes[vertice]:
			del self.adyacentes[vertice]


	def obtenerAdyacentes(self):
		a = []
		for v in self.adyacentes.values():
			a.append(v[0])
		return a


	def obtenerNumero(self):
		return self.numero


	def esIgualA(self, otroVertice):
		return self.numero == otroVertice.obtenerNumero()	
