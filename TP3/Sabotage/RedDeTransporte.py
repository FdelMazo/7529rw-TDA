from Vertice import *
from Arista import *
from dfs import *

class RedDeTransporte:
	'''
	Para esta red de transporte, se considera un grafo dirigido con un único 
	vértice sin aristas incidentes, llamado fuente, y un único vértice sin aristas 
	salientes, llamado sumidero.

	Las capacidades se consideran números enteros positivos, y se asume que cada
	nodo tiene al menos una arista incidente.
	'''

	def __init__(self):
		self.vertices = {}
		self.aristas = {}
		self.fuente = Vertice(0)
		self.sumidero = Vertice(1)
		
		self.vertices[0] = self.fuente
		self.vertices[1] = self.sumidero
	
	
	def __str__(self):
		return dfs(self)
	
	
	def obtenerFuente(self):
		return self.fuente


	def obtenerSumidero(self):
		return self.sumidero
	
	
	def agregarVertice(self, numero):
		'''
		El conjunto de vertices es un diccionario.
		'''
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
			self.vertices[numero]
		
		except KeyError: 
			self.agregarVertice(numero)
		
		finally:
			return self.vertices[numero]


	def agregarArista(self, numeroOrigen, numeroDestino, peso = 1):
		''' 
		Agrega una arista a la red. Si los vértices parametrizados no
		existen, los crea.
		
		El conjunto de aristas es un diccionario de diccionarios de 
		listas de uniones entre vértices.
		
		El primer diccionario representa las aristas del vértice origen
		y el segundo la lista de aristas que inciden en un destino particular.
		Se guardan en formato de listas por si existen varias con el mismo
		origen y destino.
		
		'''
		verticeOrigen = self.darVertice(numeroOrigen)
		verticeDestino = self.darVertice(numeroDestino)
		numOrigen = verticeOrigen.obtenerNumero()
		numDestino = verticeDestino.obtenerNumero()
		
		try: self.aristas[numOrigen]
		
		except KeyError: self.aristas[numOrigen] = {}
			
		finally:
			
			try: 
				self.aristas[numOrigen][numDestino]
			
			except KeyError: 
				self.aristas[numOrigen][numDestino] = []
				verticeOrigen.agregarAdyacente(verticeDestino)
			
			self.aristas[numOrigen][numDestino].append(
			Arista(verticeOrigen, verticeDestino, peso) )
			
		
	def obtenerVertice(self, numero):
		
		try:
			return self.vertices[numero]
			
		except KeyError:
			return None


	def obtenerVertices(self):
		return list(self.vertices.values())
	

	def obtenerAristasDesdeHasta(self, numOrigen, numDestino):
		
		try:
			return self.aristas[numOrigen][numDestino]
		
		except KeyError:
			return None
	

	def obtenerAristas(self, numOrigen = -1):
		listaAristasOrigen = []
		
		if numOrigen > 0:
			for listaAristas in self.aristas[numOrigen].values():
				listaAristasOrigen += listaAristas

		else:
			for conjuntoAristas in self.aristas.values():
				for listaAristas in conjuntoAristas.values():
					listaAristasOrigen += listaAristas
				
		return listaAristasOrigen


	def tieneArista(self, arista):
		
		v1 = arista.obtenerOrigen().obtenerNumero()
		v2 = arista.obtenerDestino().obtenerNumero()
		
		try:
			self.aristas[v1][v2]
			return True
		
		except KeyError:
			return False
