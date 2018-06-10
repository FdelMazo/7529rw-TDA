def subsetLessThan(lista, objetivo, cantidadLanzaderas):
	"""Modificacion del clasico problema donde dado una lista de numeros se devuelve el subconjunto continuo que sume el numero pedido
	En este caso, dado una lista de numeros devuelve el mayor subconjunto que sea menor o igual al numero pedido
	Cada elemento de la lista se multiplica por la cantidad de lanzaderas, porque se intenta maximizar los turnos en los que si un jugador ataca con todas sus lanzaderas al mismo barco, sobreviva
	"""
	listaMultiplicada = [i*cantidadLanzaderas for i in lista]
	if sum(listaMultiplicada) <= objetivo:
		return lista
	if len(listaMultiplicada) == 1 and sum(listaMultiplicada) > objetivo: return None
	for subset in (lista[:-1], lista[1:]):
		resultado = subsetLessThan(subset, objetivo, cantidadLanzaderas)
		return resultado

def elegirPosicionesBarcos(matriz, barcos, cantidadLanzaderas):
	for i,fila in enumerate(matriz):
		subsetsPosibles = []
		for j in range(len(fila)):
			subset = subsetLessThan(fila[j:], barcos[i].getVida(), cantidadLanzaderas)
			if subset: subsetsPosibles.append(subset)

		if not subsetsPosibles:
			minimoValor = min(fila)
			barcos[i].setPosicion(fila.index(minimoValor), i)
			continue
		subsetsPosibles = [subset for subset in subsetsPosibles if len(subset) == len(max(subsetsPosibles, key=len))]
		mejorSubset = min(subsetsPosibles,key=sum)
		primerValor = mejorSubset[0]
		x,y = fila.index(primerValor), i
		barcos[i].setPosicion(x,y)

	return