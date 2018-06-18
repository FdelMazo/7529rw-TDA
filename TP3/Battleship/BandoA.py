def elegirMejorColumna(lista, objetivo, cantidadLanzaderas):
	lista = [x * cantidadLanzaderas for x in lista]
	hileraAcumulada,mejorHilera,indice,sumatoria = [], [], 0,0
	for i,elem in enumerate(lista):
		hileraAcumulada.append(elem)
		sumatoria+=elem
		if sumatoria>objetivo:
			hileraAcumulada.pop()
			if len(hileraAcumulada) > len(mejorHilera):
				mejorHilera = hileraAcumulada
				indice = i - (len(mejorHilera))
			hileraAcumulada = []
			sumatoria = 0
	if len(hileraAcumulada) > len(mejorHilera):
		indice = len(hileraAcumulada) - 1
	if not mejorHilera: return lista.index(min(lista))
	return indice

def setPosiciones(matriz, barcos, cantidadLanzaderas):
	for y,fila in enumerate(matriz):
		x = elegirMejorColumna(fila, barcos[y].getVida(), cantidadLanzaderas)
		barcos[y].setPosicion(x, y)