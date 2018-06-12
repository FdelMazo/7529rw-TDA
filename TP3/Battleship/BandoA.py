def subsetLessThan(lista, objetivo, cantidadLanzaderas):
	"""Modificacion del clasico problema donde dado una lista de numeros se devuelve el subconjunto continuo que sume el numero pedido (subset sum)
	En este caso, dado una lista de numeros devuelve el subconjunto mas largo que sea menor o igual al objetivo pedido
	En particular, en esta implementacion, cada elemento de la lista se multiplica por la cantidad de lanzaderas, porque se intenta maximizar los turnos en los que si un jugador ataca con todas sus lanzaderas al mismo barco, sobreviva
	Devuelve None si no se encuentra ni una combinacion de dos elementos
	"""
	listaMultiplicada = [i*cantidadLanzaderas for i in lista]
	if sum(listaMultiplicada) <= objetivo:
		return lista
	if len(listaMultiplicada) == 1 and sum(listaMultiplicada) > objetivo: return None
	for subset in (lista[:-1], lista[1:]):
		resultado = subsetLessThan(subset, objetivo, cantidadLanzaderas)
		return resultado

def elegirPosicionesBarcos(matriz, barcos, cantidadLanzaderas):
	posiciones = []
	for i,fila in enumerate(matriz):
		subsetsPosibles = []
		for j in range(len(fila)):
			# Partiendo de cada elemento, busco todos los subsets mas largos para estirar la vida de mi barco
			subset = subsetLessThan(fila[j:], barcos[i].getVida(), cantidadLanzaderas)
			if subset: subsetsPosibles.append(subset)
		if not subsetsPosibles:
			# Si en el tablero no hay ni una posible hilera de casilleros donde puedo estirar la vida, simplemente lo pongo en el valor mas chico
			# Lease, un barco de vida 500 donde todos sus casilleros son de 400, es indiferente donde lo ponga
			minimoValor = min(fila)
			x,y = fila.index(minimoValor), i
			posiciones.append((x,y))
			continue
		# De lo anterior, calculo el mas largo
		subsetsPosibles = [subset for subset in subsetsPosibles if len(subset) == len(max(subsetsPosibles, key=len))]
		# De los mas largos, calculo el que menos daño produzca
		mejorSubset = min(subsetsPosibles,key=sum)
		# Lo coloco en el primer valor de la hilera
		primerValor = mejorSubset[0]
		x,y = fila.index(primerValor), i
		posiciones.append((x, y))
	return posiciones

def setPosiciones(matriz, barcos, cantidadLanzaderas):
	posiciones = elegirPosiciones(matriz, barcos, cantidadLanzaderas)
	for i, posicion in enumerate(posiciones):
		barcos[i].setPosicion(*posicion)