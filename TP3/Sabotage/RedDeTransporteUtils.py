def dfs(red):
	''' 
	Recorrido por ramas/ en profundidad de un grafo.
	Devuelve un string con el formato del recorrido realizado.
	'''
	visitados, padre = {}, {}
	recorrido, recorridoStr = [], []
	
	for v in red.obtenerVertices():
		
		if v not in visitados:
			padre[v] = None
			recorridoStr.append('\n' + str(v))
			dfs_visitar(red, v, visitados, padre, recorrido, recorridoStr)
	
	strRecorrido = ''
	
	for c in recorrido:
		strRecorrido += c
		
	return strRecorrido
	

def dfs_visitar(red, v, visitados, padre, recorrido, recorridoStr):
	visitados[v] = True
	
	for w in v.obtenerAdyacentes():
		
		if w not in visitados:
			padre[w] = v
			recorrido.append(red.obtenerArista(v, w))
			recorridoStr.append(' -> ' + str(w))
			dfs_visitar(w, visitados, padre, recorrido)
	
	return recorrido


def hayCaminosPosibles(red, flujo):	
	for a in red.obtenerAristas(red.obtenerFuente()):
		if flujo[a] < a.obtenerPeso():
			return True
	
	return False
		

def inicializarFlujo(camino, flujo):
	for a in camino:
		try: flujo[a]
		except IndexError: flujo[a] = 0


def obtenerCamino(red):
	''' 
	Pre: el grafo parametrizado es una red de flujo válida.
	Devuelve una sucesión de aristas que conecten la fuente con el sumidero. 
	'''
	padre[red.obtenerFuente()] = None
	return dfs_visitar(red.obtenerFuente(), {}, padre, recorrido, [])
	 

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

	
		
def actualizarFlujo(flujo, camino):
	
	bottleneck = obtenerAristaMinima(camino).obtenerPeso()
	
	for a in camino:
		
		if(a.esDeRegresion())
			flujo[a] -= bottleneck
		else
			flujo[a] += bottleneck
	
	return flujo


def flujoMaximo(red):

	flujo = {}
	redResidual = red
	
	while hayCaminosPosibles(redResidual, flujo):
		''' Se asume que como el grafo parametrizado es una red,
		el camino devuelto termina en el sumidero.'''
		camino = obtenerCamino(redResidual)
		inicializarFlujo(camino, flujo)
		flujo = actualizarFlujo(flujo, camino)
		''' ACTUALIZAR EL GRAFO RESIDUAL'''

	return flujo
