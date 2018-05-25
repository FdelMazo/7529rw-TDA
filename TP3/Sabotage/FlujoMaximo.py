
def obtenerCamino(red, flujo):
	
	visitados = []
	adyacentesV = []
	camino = {}
	verticeActual = red.obtenerFuente()
	vistiados.append(verticeActual)
	verticeEncontrado = True

	while not set(red.obtenerFuente().obtenerAdyacentes()).issubset( 
	set(visitados) ) and ( verticeActual is not red.obtenerSumidero() ):
		
		if verticeEncontrado: 
			verticeEncontrado = False
		
		else:
			camino = []
			verticeActual = red.obtenerFuente()
		
		adyacentesV = verticeActual.obtenerAdyacentes()
		
		for v in adyacentesV:
			
			a = red.obtenerArista(verticeActual, v)
			
			if ( a.obtenerPeso() > 0 ) and 
			(not a.esDeRegresion) and (v not in visitados):
				verticeEncontrado = True
				vistiados.append(v)
				camino.append(a)
				verticeActual = v
				break
	
	return camino
		

def inicializarFlujo(red, flujo):
	for a in red.obtenerAritas(): flujo[a] = 0


def obtenerAristaMinima(camino):
	''' Devuelve la arista con menos peso del camino parametrizado'''
	
	try: 
		aristaMin = camino[0]
		 
		for a in camino:
			if( a.obtenerPeso() < aristaMin.obtenerPeso() )
				aristaMin = a
	
	return aristaMin
		 
	except IndexError: 
		raise ValueError("Camino vacío.")


def actualizarFlujo(camino, flujo):
	
	bottleneck = obtenerAristaMinima(camino).obtenerPeso()
	
	for a in camino:
		
		if(a.esDeRegresion())
			flujo[a] -= bottleneck
		else
			flujo[a] += bottleneck
	
	return flujo


def actualizarRedResidual(red, flujo):
	
	for a in red.obtenerAristas():
		
		difFlujo = a.obtenerPeso() - f[a]
		
		if f[a]:
			
			regresion_a = red.obtenerArista(a.obtenerDestino(), a.obtenerOrigen()
			pesoActualRegresion = a.obtenerPeso() - difFlujo
			a.setPeso(difFlujo)
			
			if not regresion_a:
				red.agregarAristaDeRegresion(a.obtenerDestino().obtenerNumero(), 
				a.obtenerOrigen().obtenerNumero(), pesoActualRegresion)
			
			else:
				regresion_a.setPeso(pesoActualRegresion)
	

def flujoMaximo(red):

	flujo = {}
	redResidual = red
	inicializarFlujo(red, flujo)
	
	while True:
		camino = obtenerCamino(redResidual, flujo)
		if not camino: break
		actualizarFlujo(camino, flujo)
		actualizarRedResidual(redResidual, flujo)

	return flujo
