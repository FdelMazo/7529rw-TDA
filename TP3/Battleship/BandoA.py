def elegirMejorColumna(lista, objetivo, cantidadLanzaderas):
	lista = [x * cantidadLanzaderas for x in lista]
	hileraAcumulada,mejorHilera,indice = [], [], 0
	for i,elem in enumerate(lista):
		hileraAcumulada.append(elem)
		if sum(hileraAcumulada)>objetivo:
			hileraAcumulada.remove(elem)
			if len(hileraAcumulada) > len(mejorHilera):
				mejorHilera = hileraAcumulada
				indice = i - (len(mejorHilera))
			hileraAcumulada = []
	if sum(hileraAcumulada) <= objetivo and len(hileraAcumulada) > len(mejorHilera):
		indice = len(hileraAcumulada) - 1
	if not mejorHilera: return lista.index(min(lista))
	return indice

def setPosiciones(matriz, barcos, cantidadLanzaderas):
	for y,fila in enumerate(matriz):
		x = elegirMejorColumna(fila, barcos[y].getVida(), cantidadLanzaderas)
		barcos[y].setPosicion(x, y)