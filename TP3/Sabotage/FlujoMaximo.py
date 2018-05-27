
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


def actualizarFlujo(red, camino, flujo, cuelloDeBotella):
	
	for a in camino:
		
		if(red.tieneArista(a)):
			flujo[a] += cuelloDeBotella
			
		else:
			flujo[a] -= cuelloDeBotella


def actualizarRedResidual(red, redResidual, flujo):
	
	for a in redResidual.obtenerAristas():
		
		difFlujo = a.obtenerPeso() - flujo[a]
		
		if ( flujo[a] and ( a.obtenerPeso()> 0 ) ):
			
			pesoActualDeRegresion = a.obtenerPeso() - difFlujo
			a.setPeso(difFlujo)
			
			try:
				''' La arista de regresión será única para el caso de múltiples
				aristas con el mismo origen y destino.'''
				regresion_a = redResidual.obtenerAristasDesdeHasta( 
				a.obtenerDestino().obtenerNumero(), 
				a.obtenerOrigen().obtenerNumero() )[0]
				regresion_a.setPeso(regresion_a.obtenerPeso() + pesoActualDeRegresion)	
			
			except TypeError:
				redResidual.agregarArista(a.obtenerDestino().obtenerNumero(), 
				a.obtenerOrigen().obtenerNumero(), pesoActualDeRegresion)
	

def FordFulkerson(red):

	flujo = {}
	cuellosDeBotella = []
	redResidual = red
	maxFlujo = 0
	
	while True:
		inicializarFlujo(redResidual, flujo)
		camino = obtenerCamino(redResidual, flujo)
		if not camino: break
		cuellosDeBotella.append(obtenerAristaMinima(camino))
		cuelloActual = cuellosDeBotella[-1].obtenerPeso()
		maxFlujo += cuelloActual
		actualizarFlujo(red, camino, flujo, cuelloActual)
		actualizarRedResidual(red, redResidual, flujo)

	return maxFlujo, cuellosDeBotella


def flujoMaximo(red):
	
	maxFlujo, cuellosDeBotella = FordFulkerson(red)
	return maxFlujo
