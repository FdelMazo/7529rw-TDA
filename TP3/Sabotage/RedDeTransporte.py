from Vertice import *
from Arista import *
from RedDeTransporteUtils import *

class RedDeTransporte:


	def __init__(self):
		self.vertices = {}
		self.aristas = {}
		self.fuente = Vertice(0)
		self.sumidero = Vertice(1)
		
		self.vertices[0] = self.fuente
		self.vertices[1] = self.sumidero
	
	
	def __str__(self):
		return dfs(self)
	
	
	def agregarVertice(self, numero):
		
		try:
			self.vertices[numero]
			raise ValueError("Ya existe un vértice con ese número.")
		
		except KeyError:
			self.vertices[numero] = Vertice(numero)


	def darVertice(self, numero):
		''' 
		Devuelve el vértice con el número especificado.
		Si no existe lo crea.
		'''
		
		try: 
			self.vertice[numero]
		
		except KeyError: 
			agregarVertice(numero)
		
		finally:
			return self.vertices[numero]


	def agregarArista(self, numeroOrigen, numeroDestino, peso = 1):
		verticeOrigen = self.darVertice(numeroOrigen)
		verticeDestino = self.darVertice(numeroDestino)
		self.aristas[ len(self.aristas) ] = Arista(verticeOrigen, verticeDestino, peso)
		verticeOrigen.agregarAdyacente(verticeDestino)
	

	def obtenerVertice(self, numero):
		
		try:
			return self.vertices[numero]
			
		except KeyError:
			return None


	def obtenerVertices(self):
		return list(self.vertices.values())
