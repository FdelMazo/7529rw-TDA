def dfs(red):
	''' 
	Recorrido por ramas/ en profundidad de un grafo.
	Devuelve un string con el formato del recorrido realizado.
	'''
	visitados = []
	recorridoStr = []
	
	for v in red.obtenerVertices():
		
		if v not in visitados:
			recorridoStr.append('\n' + str(v))
			dfs_visitar(v, visitados, recorridoStr)

	strRecorrido = ''
	
	for c in recorridoStr:
		strRecorrido += c
		
	return strRecorrido
	

def dfs_visitar(v, visitados, recorridoStr):
	
	visitados.append(v)
	
	for w in v.obtenerAdyacentes():
		
		if w not in visitados:
			recorridoStr.append(' -> ' + str(w))
			dfs_visitar(w, visitados, recorridoStr)
