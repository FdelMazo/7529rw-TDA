def dfs(red):
	''' 
	Recorrido por ramas/ en profundidad de un grafo.
	Devuelve un string con el formato del recorrido realizado.
	'''
	visitados, padre = {}, {}
	recorrido = []
	
	for v in red.obtenerVertices():
		
		if v not in visitados:
			padre[v] = None
			recorrido.append('\n' + str(v))
			dfs_visitar(v, visitados, padre, recorrido)
	
	strRecorrido = ''
	
	for c in recorrido:
		strRecorrido += c
		
	return strRecorrido
	

def dfs_visitar(v, visitados, padre, recorrido):
	visitados[v] = True
	
	for w in v.obtenerAdyacentes():
		
		if w not in visitados:
			padre[w] = v
			recorrido.append(' -> ' + str(w))
			dfs_visitar(w, visitados, padre, recorrido)
