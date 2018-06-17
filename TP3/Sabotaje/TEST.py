from Vertice import *
from Arista import *
from AntiSabotaje import *  

class RedDeTransporte:
	'''
	Para esta red de transporte, se considera un grafo dirigido con un único 
	vértice sin aristas incidentes, llamado fuente, y un único vértice sin aristas 
	salientes, llamado sumidero.

	Las capacidades se consideran números naturales, y se asume que cada
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
		redStr = ''
		for a in self.obtenerAristas():
			redStr += str(a)
		return redStr


	def obtenerFuente(self):
		return self.fuente


	def obtenerSumidero(self):
		return self.sumidero
	
	
	def esIgualA(self, otraRed):
		
		try: 
			for a in otraRed.obtenerAristas():
				match = False
				numOrigen = a.obtenerOrigen().obtenerNumero()
				numDestino = a.obtenerDestino().obtenerNumero()
				
				for a2 in self.aristas[numOrigen][numDestino]:
					if a.esIgualA(a2):
						match = True
						break
						
				if not match:
					return False
							
			for v in otraRed.obtenerVertices():
				numVertice = v.obtenerNumero()
				
				if not self.vertices[numVertice].esIgualA(v):
					return False
				
				return True
			
		except KeyError:
			return False
		
		
	def agregarVertice(self, numero, info = None):
		'''
		El conjunto de vertices es un diccionario.
		'''
		try:
			self.vertices[numero]
			raise ValueError("Ya existe un vértice con ese número.")
		
		except KeyError:
			self.vertices[numero] = Vertice(numero, info)
			return self.vertices[numero]


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


	def agregarArista(self, numeroOrigen, numeroDestino, peso = 1, identificador = None):
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
		
		try: self.aristas[numeroOrigen]
		
		except KeyError: self.aristas[numeroOrigen] = {}
			
		finally:
			
			try: 
				self.aristas[numeroOrigen][numeroDestino]
			
			except KeyError: 
				self.aristas[numeroOrigen][numeroDestino] = []
				
			verticeOrigen.agregarAdyacente(verticeDestino)
			arista = Arista(verticeOrigen, verticeDestino, peso, identificador)
			if (not identificador): arista.setId( id(arista) )
			self.aristas[numeroOrigen][numeroDestino].append( arista )
			return arista
			

	def agregarAristaInversa(self, arista):
		idArista = arista.obtenerId()
		numOrigen = arista.obtenerOrigen().obtenerNumero()
		numDestino = arista.obtenerDestino().obtenerNumero()
		return self.agregarArista(numDestino, numOrigen, 0, idArista)
	

	def obtenerAristaInversa(self, arista):
		idArista = arista.obtenerId()
		numOrigen = arista.obtenerOrigen().obtenerNumero()
		numDestino = arista.obtenerDestino().obtenerNumero()
		
		try:
			aristasPosibles = self.aristas[numDestino][numOrigen]
			for a in aristasPosibles:
				if ( ( a.obtenerId() ) and 
				( a.obtenerId() == idArista ) ):
					return a
		
		except KeyError:
			return None


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
			return []
	
	
	def obtenerArista(self, numOrigen, numDestino, identificador):
		aristasPosibles = self.obtenerAristasDesdeHasta(numOrigen, numDestino)
		
		for a in aristasPosibles:
			if a.obtenerId() == identificador:
				return a
		
		return None
	
	
	def obtenerAristas(self, numOrigen = -1):
		listaAristasOrigen = []
		
		if numOrigen >= 0:
			for listaAristas in self.aristas[numOrigen].values():
				listaAristasOrigen += listaAristas

		else:
			for conjuntoAristas in self.aristas.values():
				for listaAristas in conjuntoAristas.values():
					listaAristasOrigen += listaAristas
				
		return listaAristasOrigen

	
	def borrarArista(self, numOrigen, numDestino, identificador):
		try:
			vOrigen = self.vertices[numOrigen]
			vDestino = self.vertices[numDestino]
			vOrigen.borrarAdyacente(vDestino)	
			arista = self.obtenerArista(numOrigen, numDestino, identificador)
			self.aristas[numOrigen][numDestino].remove(arista)
			return arista
		
		except:
			raise ValueError("Arista Inexistente.")

	
	def estaConectada(self):
		verticesAccesibles = llegarAlSumidero(self)
		
		if ( ( self.sumidero.obtenerNumero() not in verticesAccesibles )
		or   ( self.fuente.obtenerNumero() not in verticesAccesibles ) ):
			return False
		
		return True
		
	
	def obtenerAristasDeCorte(self):
		
		aristasDeCorte = []
		
		for a in self.obtenerAristas():
			numOrigen = a.obtenerOrigen().obtenerNumero()
			numDestino = a.obtenerDestino().obtenerNumero()
			pesoArista = a.obtenerPeso()
			identificador = a.obtenerId()
			aristaBorrada = self.borrarArista(numOrigen, numDestino, identificador)
			
			if not self.estaConectada():
				aristasDeCorte.append(aristaBorrada)
			
			self.agregarArista(numOrigen, numDestino, pesoArista, identificador)

		return aristasDeCorte


	def tieneArista(self, numOrigen, numDestino):
		
		try:
			self.aristas[numOrigen][numDestino]
			return True
		
		except KeyError:
			return False


def obtenerAristaIgualIncluida(arista, aristas):
	
	for a in aristas:
		if arista.esIgualA(a):
			return a
	
	return None


def llegarAlSumidero(red):
	''' 
	Recorrido por ramas/ en profundidad de una red.
	Devuelve un camino al sumidero desde la fuente.
	'''
	visitados = [red.obtenerFuente().obtenerNumero()]
	
	for v in red.obtenerFuente().obtenerAdyacentes():
		if 1 in visitados:
			break
		
		if v.obtenerNumero() not in visitados:
			llegarAlSumidero_visitar(v, visitados)
		
	return visitados
	

def llegarAlSumidero_visitar(v, visitados):
	visitados.append(v.obtenerNumero())
	
	for w in v.obtenerAdyacentes():
		if 1 in visitados:
			break
		
		if w.obtenerNumero() not in visitados:
			llegarAlSumidero_visitar(w, visitados)

red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa39.map")
aristasProtegidas = proteger2Aristas(red)