from RedDeTransporte import *


def imprimirCamino(camino):
	for a in camino:
		print(a)


def imprimirFlujo(flujo):
	for key,value in flujo.items():
		print( str(a) + '  -  ' + str(value) )


def obtenerCamino(red, flujo):
	
	visitadas = []
	adyacentesV = []
	camino = []
	verticeActual = red.obtenerFuente()
	aristaActual = None
	
	''' Condiciones de corte: se visitaron todos las aristas salientes 
	de la fuente, o el vértice actual es el sumidero''' 
	while not set(red.obtenerAristas(red.obtenerFuente().obtenerNumero())).issubset( 
	set(visitadas))  and ( verticeActual is not red.obtenerSumidero() ):
		
		for a in red.obtenerAristas(verticeActual.obtenerNumero()):
			if (a not in visitadas) and (a.obtenerPeso() > 0):
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
	
	for a in red.obtenerAristas(): 
		
		try: flujo[a]
		except KeyError: flujo[a] = 0


def obtenerAristaMinima(camino):
	''' Devuelve la arista con menos peso del camino parametrizado'''
	
	try: 
		aristaMin = camino[0]
		 
		for a in camino:
			if ( a.obtenerPeso() < aristaMin.obtenerPeso() ):
				aristaMin = a
	
		return aristaMin
		 
	except IndexError: 
		raise ValueError("Camino vacío.")


def flujoActualizado(red, camino, flujo, cuelloDeBotella):
	
	flujoActual = {}
	
	for a in camino:
		
		if( red.tieneArista( a.obtenerOrigen().obtenerNumero(),
		a.obtenerDestino().obtenerNumero() ) ):
			flujoActual[a] = flujo[a] + cuelloDeBotella
			
		else:
			flujoActual[a] = flujo[a] - cuelloDeBotella

	return flujoActual


def actualizarRedResidual(red, redResidual, flujo):
	
	for a, valorDeFlujo in flujo.items():
	
		aristaOriginal = red.obtenerAristaConPeso(
		a.obtenerOrigen().obtenerNumero(),
		a.obtenerDestino().obtenerNumero(), 
		a.obtenerPeso())			
		
		if (aristaOriginal):
			a.setPeso(aristaOriginal.obtenerPeso() - valorDeFlujo) 
			numOrigen = a.obtenerOrigen().obtenerNumero()
			numDestino = a.obtenerDestino().obtenerNumero()
			
			if (not redResidual.obtenerAristasDesdeHasta(numOrigen, numDestino)):
				aristaResidual = redResidual.agregarArista( numOrigen, 
				numDestino, valorDeFlujo)
				flujo[aristaResidual] = 0
			
		else:
			a.setPeso(valorDeFlujo)	


def actualizarFlujoA(flujo, flujoActual):
	for a, valorFlujo in flujoActual.items():
		flujo[a] = valorFlujo


def FordFulkerson(red, mostrarCamino = False):

	flujo = {}
	cuellosDeBotella = []
	aristasRed = red.obtenerAristas()
	redResidual = RedDeTransporte()
	redResidual.agregarAristas(aristasRed)
	maxFlujo = 0
	inicializarFlujo(redResidual, flujo)
	
	while True:
		camino = obtenerCamino(redResidual, flujo)
		if not camino: break
		if mostrarCamino: imprimirCamino(camino)
		cuellosDeBotella.append(obtenerAristaMinima(camino))
		cuelloActual = cuellosDeBotella[-1].obtenerPeso()
		maxFlujo += cuelloActual
		flujoActual = flujoActualizado(red, camino, flujo, cuelloActual)
		actualizarRedResidual(red, redResidual, flujoActual)
		actualizarFlujoA(flujo, flujoActual)
	
	return maxFlujo, cuellosDeBotella


def flujoMaximo(red, mostrarCamino = False):
	
	maxFlujo, cuellosDeBotella = FordFulkerson(red, mostrarCamino)
	return maxFlujo




red = RedDeTransporte()
red.agregarArista(0, 2, 20)
red.agregarArista(2, 1, 10)
red.agregarArista(0, 3, 10)
red.agregarArista(2, 3, 30)
red.agregarArista(3, 1, 20)
flujoMaximo(red, True)
