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
		
		try: 
			red.obtenerAristas(verticeActual.obtenerNumero())
		except KeyError:
			camino = []
			break
		
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


def obtenerAristaMinima(red, camino):

	try: 
		aristaMin = camino[0]
		 
		for a in camino:
			if ( a.obtenerPeso() < aristaMin.obtenerPeso() ):
				aristaMin = a
	
			if ( a.obtenerPeso() == aristaMin.obtenerPeso() ):
				aOriginal = red.obtenerArista(a.obtenerOrigen().obtenerNumero(),
				a.obtenerDestino().obtenerNumero(),
				a.obtenerId() )
				
				aristaMinOriginal = red.obtenerArista(
				aristaMin.obtenerOrigen().obtenerNumero(),
				aristaMin.obtenerDestino().obtenerNumero(),
				aristaMin.obtenerId() )
				
				if(aOriginal and aristaMinOriginal):
					if ( aOriginal.obtenerPeso() < 
					aristaMinOriginal.obtenerPeso() ):
						aristaMin = a
					
				elif aOriginal:
					aristaMin = a
									
		return aristaMin
		 
	except IndexError: 
		raise ValueError("Camino vacío.")


def actualizarCuellosDeBotella(cuellosDeBotella, cuelloDeBotella, redOriginal):
	
	numOrigen = cuelloDeBotella.obtenerOrigen().obtenerNumero()
	numDestino = cuelloDeBotella.obtenerDestino().obtenerNumero()
	identificador = cuelloDeBotella.obtenerId()

	aristaOriginal = redOriginal.obtenerArista(numOrigen, numDestino, identificador)
	aristaInversa = redOriginal.obtenerArista(numDestino, numOrigen, identificador)
	
	if (aristaOriginal) and (aristaOriginal not in cuellosDeBotella):
		cuellosDeBotella.append(aristaOriginal)
	
	elif (aristaInversa) and (aristaInversa not in cuellosDeBotella):
		cuellosDeBotella.append(aristaInversa)


def FordFulkerson(redOriginal):
	
	flujo = {}
	capacidad = {}
	maxFlujo = 0
	cuellosDeBotella = []
	
	redResidual = RedDeTransporte()
	inicializarRedResidual(redResidual, redOriginal.obtenerAristas())
	inicializarFlujo(redResidual, flujo)
	inicializarCapacidad(redResidual, capacidad)
	
	while True:
		camino = obtenerCamino(redResidual, flujo)
		if not camino: break
		
		cuelloDeBotella = obtenerAristaMinima(redOriginal, camino)
		actualizarCuellosDeBotella(cuellosDeBotella, cuelloDeBotella, redOriginal)
		cuelloActual = cuelloDeBotella.obtenerPeso()
		maxFlujo += cuelloActual

		for a in camino:
			numOrigen = a.obtenerOrigen().obtenerNumero()
			numDestino = a.obtenerDestino().obtenerNumero()	
			aristaInversa = redResidual.obtenerAristaInversa(a)
			
			if (redOriginal.tieneArista(numOrigen, numDestino)):
				flujo[a] += cuelloActual
				a.setPeso(capacidad[a] - flujo[a])
				aristaInversa.setPeso(flujo[a])
				
			else:
				flujo[aristaInversa] -= cuelloActual
				a.setPeso(flujo[aristaInversa])
				aristaInversa.setPeso(capacidad[aristaInversa] - flujo[aristaInversa])				
			

	return maxFlujo, cuellosDeBotella 


def flujoMaximo(red):
	
	maxFlujo, cuellosDeBotella = FordFulkerson(red)
	return maxFlujo
