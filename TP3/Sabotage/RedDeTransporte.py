from Vertice import *
from Arista import *
from bfs import *


class RedDeTransporte:
'''
Para esta red de transporte, se considera un grafo dirigido con un único 
vértice sin aristas incidentes, llamado fuente, y un único vértice sin aristas 
salientes, llamado sumidero.
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
			self.vertice[numero]
		
		except KeyError: 
			agregarVertice(numero)
		
		finally:
			return self.vertices[numero]


	def agregarArista(self, numeroOrigen, numeroDestino, peso = 1, esAristaDeRegresion = False):
	''' 
		El conjunto de aristas es un diccionario de diccionarios de 
		listas de uniones entre vértices.
		
		El primer diccionario representa las aristas del vértice origen
		y el segundo las aristas que inciden en un destino particular.
	'''
		if (numeroDestino == self.fuente.numero):
			raise ValueError("La fuente no puede tener aristas entrantes")
		
		elif (numeroOrigen == self.sumidero.numero):
			raise ValueError("El sumidero no puede tener aristas salientes")
		
		if (peso < 0)
			raise ValueError("El peso no puede ser negativo")
		
		verticeOrigen = self.darVertice(numeroOrigen)
		verticeDestino = self.darVertice(numeroDestino)
		numOrigen = verticeOrigen.obtenerNumero()
		numDestino = verticeDestino.obtenerNumero()
		
		try: 
			self.aristas[numOrigen][numDestino]
		
		except KeyError:
			self.aristas[numOrigen][numDestino] = []
		
		finally:
			if esAristaDeRegresion:
				self.aristas[numOrigen][numDestino].append(
				AristaDeRegresion(verticeOrigen, verticeDestino, peso) )
			
			else:	
				self.aristas[numOrigen][numDestino].append( 
				Arista(verticeOrigen, verticeDestino, peso) )
		
		verticeOrigen.agregarAdyacente(verticeDestino)
	

	def agregarAristaDeRegresion(self, numeroOrigen, numeroDestino, peso = 1):
		agregarArista(self, numeroOrigen, numeroDestino, peso, True):
	

	def obtenerVertice(self, numero):
		
		try:
			return self.vertices[numero]
			
		except KeyError:
			return None


	def obtenerArista(self, v1, v2, peso = -1):
		
		try:
			aristasPosibles = self.aristas[v1.obtenerNumero()][v2.obtenerNumero()]
			
			if(peso < 0)
				return aristasPosibles[0]
			
			return aristasPosibles[peso]
		
		except KeyError:
			return None
				

	def obtenerVertices(self):
		return list(self.vertices.values())


	def obtenerAristas(self, origen):
		listaAristasOrigen = []
		
		for conjuntoAristas in self.aristas[origen.obtenerNumero()]:
			for listaAristas in conjuntAristas.values():
				listaAristasOrigen += listaAristasOrigen
				
		return listaAristasOrigen


	def obtenerFuente(self)
		return self.fuente
