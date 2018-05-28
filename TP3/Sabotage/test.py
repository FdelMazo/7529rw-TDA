from RedDeTransporte import *


def imprimirCamino(camino):
	for a in camino:
		print(a)


def imprimirFlujo(flujo):
	for key,value in flujo.items():
		print( str(a) + '  -  ' + str(value) )


def inicializarRedResidual(redResidual, aristasRed):
	for a in aristasRed:
		numOrigen = a.obtenerOrigen().obtenerNumero(),
		numDestino = a.obtenerDestino().obtenerNumero(),
		peso = a.obtenerPeso()
		redResidual.agregarArista(numOrigen, numDestino, peso)
		redResidual.agregarArista(numDestino, numOrigen, 0)


def hayCaminoPosible(red):
	
	for a in red.obtenerAristas(red.obtenerFuente().obtenerNumero()):
		if a.obtenerPeso() > 0:
			return True
	
	return False


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
	''' Devuelve la arista con menos peso del camino parametrizado'''
	
	try: 
		aristaMin = camino[0]
		 
		for a in camino:
			if ( a.obtenerPeso() < aristaMin.obtenerPeso() ):
				aristaMin = a
	
		return aristaMin
		 
	except IndexError: 
		raise ValueError("Camino vacío.")


def flujoActualizado(red, redResidual, camino, flujo, cuelloDeBotella, capacidad):
	
	flujoActual = {}
	
	for a in camino:
		
		numOrigen = a.obtenerOrigen().obtenerNumero()
		numDestino = a.obtenerDestino().obtenerNumero()
		
		if( red.tieneArista( numOrigen, numDestino) ):
			flujoActual[a] = flujo[a] + cuelloDeBotella
			a.setPeso(capacidad[a] - flujoActual[a])
			if (not redResidual.obtenerAristasDesdeHasta(numDestino, numOrigen)):
				aristaResidual = redResidual.agregarArista( numDestino, 
				numOrigen, flujoActual[a])
			
		else:
			aOriginal = redResidual.obtenerAristasDesdeHasta( numDestino, numOrigen )[0]
			flujoActual[aOriginal] = flujo[aOriginal] - cuelloDeBotella
			aOriginal.setPeso(capacidad[aOriginal] - flujoActual[aOriginal])
			a.setPeso(flujoActual[aOriginal])

	return flujoActual


def actualizarRedResidual(red, redResidual, flujo, capacidad):
	
	flujoAux = dict(flujo)
	
	for a, valorDeFlujo in flujoAux.items():
	
		numOrigen = a.obtenerOrigen().obtenerNumero()
		numDestino = a.obtenerDestino().obtenerNumero()

		if (flujo[a] > 0):
			a.setPeso(capacidad[a] - valorDeFlujo)
			if (not redResidual.obtenerAristasDesdeHasta(numDestino, numOrigen)):
				aristaResidual = redResidual.agregarArista( numDestino, 
				numOrigen, valorDeFlujo)
				flujo[aristaResidual] = 0
			
		else:
			aResidual = redResidual.obtenerAristasDesdeHasta( numDestino, numOrigen )[0]
			aResidual.setPeso(valorDeFlujo)
			a.setPeso(capacidad[a] - valorDeFlujo)	


def actualizarFlujoA(flujo, flujoActual):
	for a, valorFlujo in flujoActual.items():
		flujo[a] = valorFlujo


def FordFulkerson(red, mostrarCamino = False):

	flujo = {}
	cuellosDeBotella = []
	aristasRed = red.obtenerAristas()
	redResidual = RedDeTransporte()
	inicializarRedResidual(redResidual, aristasRed)
	maxFlujo = 0
	inicializarFlujo(redResidual, flujo)
	capacidad = {}
	inicializarCapacidad(redResidual, capacidad)
	
	while True:
		camino = obtenerCamino(redResidual, flujo)
		if not camino: break
		if mostrarCamino: imprimirCamino(camino)
		cuellosDeBotella.append(obtenerAristaMinima(camino))
		cuelloActual = cuellosDeBotella[-1].obtenerPeso()
		maxFlujo += cuelloActual
		
		for a in camino:
			numOrigen = a.obtenerOrigen().obtenerNumero()
			numDestino = a.obtenerDestino().obtenerNumero()
			aristaInversa = red.obtenerAristasDesdeHasta(numDestino, numOrigen)
			
			if (red.tieneArista(numOrigen, numDestino)):
				flujo[a] += cuelloActual
				flujo[aristaInversa] -= cuelloActual
				a.setPeso(capacidad[a] - flujo[a])
				aristaInversa.setPeso(flujo[a])
		
			else:
				flujo[aristaInversa] += cuelloActual
				flujo[a] -= cuelloActual
				aristaInversa.setPeso(capacidad[a] - flujo[a])
				a.setPeso(flujo[a])
		
		'''flujoActual = flujoActualizado(red, redResidual, camino, flujo, cuelloActual, capacidad)
		actualizarRedResidual(red, redResidual, flujoActual, capacidad)
		actualizarFlujoA(flujo, flujoActual)
		'''
	
	return maxFlujo, cuellosDeBotella

def flujoMaximo(red, mostrarCamino = False):
	
	maxFlujo, cuellosDeBotella = FordFulkerson(red, mostrarCamino)
	return maxFlujo



red = RedDeTransporte()
red.agregarArista(0, 1, 1)
red.agregarArista(0, 1, 1)
red.agregarArista(0, 1, 1)
flujoMaximo(red)