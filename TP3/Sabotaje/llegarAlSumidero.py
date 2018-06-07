from RedDeTransporte import * 

def llegarAlSumidero(red):
	''' 
	Recorrido por ramas/ en profundidad de una red.
	Devuelve un camino al sumidero.
	'''
	visitados = []
	vertices = red.obtenerVertices()
	vertices.remove(red.obtenerSumidero())
	
	for v in vertices:
		
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
