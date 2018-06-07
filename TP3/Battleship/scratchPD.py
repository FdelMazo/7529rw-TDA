from copy import copy
from Juego import Juego
from Barco import Barco
from copy import copy
ARCHIVO = 'grilla.coords'

def listaOptima(listas):
	if isinstance(listas[0], list) and isinstance(listas[0][0],list):
		listas = [item for sublist in listas for item in sublist]

	listasSinDup = []
	for l in listas:
		if l not in listasSinDup: listasSinDup.append(l)
	listas = listasSinDup

	atributos = []
	for lista in listas:
		sumatoria, cantidadDerribados = sum([a for a in lista if a > 0]), len([a for a in lista if a <= 0])
		atributos.append((sumatoria, cantidadDerribados))
	opt = 0
	for i in range(len(listas)):
		if atributos[i][1] > atributos[opt][1]:
			opt = i
		elif atributos[i][1] == atributos[opt][1] and atributos[i][0] < atributos[opt][0]:
			opt = i

	return listas[opt]

def elegirTargets(juego):
	"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy)
	Devuelve una lista de barcos a los que ataca cada lanzadera"""

	barcos = juego.getBarcos()
	cantLanzaderas = juego.getCantidadLanzaderas()

	posibilidadesIni = [[b.getVida() for b in barcos] for i in range(len(barcos))]
	posibilidadesTotales = [posibilidadesIni for i in range(cantLanzaderas)]


	for i in range(cantLanzaderas):
		posibilidadLocalIni = copy(listaOptima(posibilidadesTotales))
		posibilidades = [posibilidadLocalIni for i in range(len(barcos))]

		for j in range(len(barcos)):
			posibilidadActual = copy(posibilidadLocalIni)
			dummyDanio = juego.getDanioCasillero(*barcos[j].getPosicion())
			posibilidadActual[j] -= dummyDanio
			posibilidades[j] = listaOptima([posibilidades[j], posibilidadActual])

		siguientePosibilidadLocalIni = copy(listaOptima([*posibilidades, *posibilidadesTotales[i]]))
		posibilidadesTotales[i] = [siguientePosibilidadLocalIni for i in range(cantLanzaderas)]


	return listaOptima(posibilidadesTotales)

matrizTablero = Juego.ArchivoToMatriz(ARCHIVO)
barcos = Juego.ArchivoToBarcos(ARCHIVO)
cantidadLanzaderas = 3

juego = Juego(matrizTablero, barcos, cantidadLanzaderas, None)
juego.setPosicionesIniciales()

print(elegirTargets(juego))