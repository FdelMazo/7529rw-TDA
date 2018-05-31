from RedDeTransporte import *


def inicializarRedResidual(redResidual, aristasRed):
	for a in aristasRed:
		numOrigen = a.obtenerOrigen().obtenerNumero()
		numDestino = a.obtenerDestino().obtenerNumero()
		idArista = a.obtenerId()
		pesoArista = a.obtenerPeso()
		arista = redResidual.agregarArista(numOrigen, numDestino, pesoArista, idArista)
		redResidual.agregarAristaInversa(arista)


def obtenerCamino(red, flujo):
	
	visitadas = []
	adyacentesV = []
	camino = []
	verticeActual = red.obtenerFuente()
	aristaActual = None
	 
	while ( verticeActual is not red.obtenerSumidero() ):
		for a in red.obtenerAristas(verticeActual.obtenerNumero()):
			if ( (a not in visitadas) and ( a.obtenerPeso() > 0 ) ):
				aristaActual = a
				visitadas.append(aristaActual)
				break
			
		if aristaActual:
				camino.append(aristaActual)
				verticeActual = a.obtenerDestino()
				aristaActual = None
			
		else:
			''' Volver al vértice anterior, si lo hay.'''
			try: verticeActual = camino.pop().obtenerOrigen()
			except IndexError: return []
			
	return camino
		

def inicializarFlujo(red, flujo):
	for a in red.obtenerAristas(): flujo[a] = 0


def inicializarCapacidad(red, capacidad):
	for a in red.obtenerAristas(): capacidad[a] = a.obtenerPeso()


def obtenerAristaMinima(camino):
	''' Devuelve la arista con menos peso del camino parametrizado.'''
	
	try: 
		aristaMin = camino[0]
		 
		for a in camino:
			if ( a.obtenerPeso() < aristaMin.obtenerPeso() ):
				aristaMin = a
	
		return aristaMin
		 
	except IndexError: 
		raise ValueError("Camino vacío.")


def FordFulkerson(redOriginal, mostrarCamino = False):
	'''
	Devuelve el flujo máximo de la red, sus cuellos de botella
	y los caminos "reales" (sin aristas de regresión) realizados
	para computar el flujo máximo.
	'''
	
	red = duplicarRed(redOriginal)
	flujo = {}
	cuellosDeBotella = []
	aristasRed = red.obtenerAristas()
	redResidual = RedDeTransporte()
	inicializarRedResidual(redResidual, aristasRed)
	maxFlujo = 0
	inicializarFlujo(redResidual, flujo)
	capacidad = {}
	inicializarCapacidad(redResidual, capacidad)
	caminos = []
	
	while True:
		camino = obtenerCamino(redResidual, flujo)
		if not camino: break
		if mostrarCamino: print(camino)
		
		cuelloDeBotella = obtenerAristaMinima(camino)
		cuelloActual = cuelloDeBotella.obtenerPeso()
		maxFlujo += cuelloActual
		
		cuellosDeBotella.append(redOriginal.obtenerArista(
		cuelloDeBotella.obtenerOrigen().obtenerNumero(),
		cuelloDeBotella.obtenerDestino().obtenerNumero(),
		cuelloDeBotella.obtenerId()
		)
		)	
		unCamino = []
		
		for a in camino:
			numOrigen = a.obtenerOrigen().obtenerNumero()
			numDestino = a.obtenerDestino().obtenerNumero()	
			aristaInversa = redResidual.obtenerAristaInversa(a)
			
			if (red.tieneArista(numOrigen, numDestino)):
				flujo[a] += cuelloActual
				a.setPeso(capacidad[a] - flujo[a])
				aristaInversa.setPeso(flujo[a])
				unCamino.append( redOriginal.obtenerArista(
				a.obtenerOrigen().obtenerNumero(),
				a.obtenerDestino().obtenerNumero(),
				a.obtenerId()
				)
				)
					
			else:
				flujo[aristaInversa] -= cuelloActual
				a.setPeso(flujo[aristaInversa])
				aristaInversa.setPeso(capacidad[aristaInversa] - flujo[aristaInversa])				
				if cuellosDeBotella: cuellosDeBotella.pop()
			
		caminos.append(unCamino)

	return maxFlujo, cuellosDeBotella, caminos 


def flujoMaximo(red, mostrarCamino = False):
	
	maxFlujo, cuellosDeBotella, caminos = FordFulkerson(red, mostrarCamino)
	return maxFlujo
