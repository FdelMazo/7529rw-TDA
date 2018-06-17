from Jugador import Jugador
from copy import copy
from heapq import heappush, heappop
import itertools


class Dyno(Jugador):
	"""
	Dyno:
		Juega partidas reducidas, y en base a esas genera nuevas partidas. Así, hasta llegar a la mejor partida.

		La reduccion consiste en partidas de una lanzadera y un barco y la matriz finita (la partida termina con el ultimo casillero)

		Entonces, iterando desde barco mas dificil de matar:
			- Busca cuales son sus partidas posibles a jugar
			- De lo que ya tenia memorizado, busca las partidas posibles para jugar con un barco mas que lo anterior
			- De las combinaciones, elige la mejor partida
	"""

	def __init__(self):
		super().__init__('Dyno')

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		matriz, barcos, cantidadLanzaderas = partidaOriginal.getMatriz(), partidaOriginal.getBarcosVivos(), partidaOriginal.getCantidadLanzaderas()

		turnosParaTodos = self.comoMatarBarcos(matriz, barcos)
		heapDeBarcosDificiles = sortPorBarcoDificilDeMatar(turnosParaTodos)
		_, barcoActualID = heappop(heapDeBarcosDificiles)
		partidasPorBarco = self.combinacionesAPartidas(barcoActualID, turnosParaTodos[barcos[barcoActualID]],cantidadLanzaderas)

		resultados = self.definirPartidaAJugar(heapDeBarcosDificiles, turnosParaTodos, partidasPorBarco, barcos,cantidadLanzaderas)

		partida, barcosRemanentes = self.jugarPartidaMatrizFinita(resultados, barcos)
		if barcosRemanentes: partida = matarBarcosRemanentes(partida, barcosRemanentes, matriz, cantidadLanzaderas)
		return partida

	def partidaOptima(self, partidas):
		"""La partida optima de una lista de partidas es la mas 'ajustada', es decir, la que mas dispara y gana lo antes posible
		De esta forma se logra que no se extienda la partida dejandola llena de lanzaderas que no disparan
		"""
		atributoPartidas = []
		for partida in partidas:
			atributoPartidas.append((partida, self.contadorTargetsVacios(partida)))
		return max(atributoPartidas, key=lambda x: -x[1])[0]

	def contadorTargetsVacios(self, partida):
		cantLanzaderas = 0
		for turno in partida:
			if turno:
				cantLanzaderas = len(turno)
				break

		contadorNones = 0
		for turno in partida:
			if turno:
				contadorNones += turno.count(None)
			else:
				contadorNones += cantLanzaderas
		return contadorNones

	def combinacionesAPartidas(self, idBarco, combinaciones, cantidadLanzaderas):
		"""Recibe una lista de turnos en los cuales disparar y los convierte en una partida valida"""
		partidas = []
		for combinacion in combinaciones:
			partida = []
			for turno in combinacion:
				while len(partida) <= turno: partida += [None]
				partida[turno] = [idBarco] + [None] * (cantidadLanzaderas - 1)
			partidas.append(partida)
		return partidas

	def combinacionesMatadoras(self, lista, objetivo):
		"""Recibe una lista de numeros y un objetivo
		Devuelve todas las combinaciones para llegar a sobrepasarlo
		Las combinaciones son unicas (sin dupicados) y ajustadas (son clavadas, no hay disparos sobrantes)"""
		listaOriginal = copy(lista)
		combs = []
		for i in range(len(lista)):
			for c in itertools.combinations(lista, i):
				if sum(c) >= objetivo:
					combs.append(list(c))
		# Saco los numeros sobrantes:Por ejemplo, si el objetivo es 10 y la lista es [6,4,7] el 7 final sobra"""
		# Saco los duplicados: No se puede hacer el metodo del set de python (meter todo en un set, que tiene elementos unicos) ya que los elementos aca son listas mismas, y las listas no son hasheables, por ende no entran en un set (si, se podrian pasar a tuplas y luego volver, pero termina siendo mas costoso)"""
		newCombs = []
		for comb in combs:
			# Hack: https://stackoverflow.com/a/34238688
			for elem in comb[:]:
				indice = comb.index(elem)
				comb.remove(elem)
				if sum(comb) >= objetivo:
					continue
				comb.insert(indice, elem)
			if comb in newCombs: continue
			newCombs.append(comb)
		# Convierte la lista a indices
		resultados = []
		for comb in newCombs:
			listaIndices = []
			for elem in comb:
				indice = listaOriginal.index(elem)
				while indice in listaIndices:
					indice += listaOriginal[indice + 1:].index(elem) + 1
				listaIndices.append(indice)
			if listaIndices not in resultados: resultados.append(listaIndices)
		return resultados

	def comoMatarBarcos(self, matriz, barcos):
		turnosParaTodos = {}
		for y, fila in enumerate(matriz):
			turnosDondeMuere = self.combinacionesMatadoras(fila, barcos[y].getVida())
			if turnosDondeMuere: turnosParaTodos[barcos[y]] = sorted(turnosDondeMuere)
		return turnosParaTodos

	def definirPartidaAJugar(self, heapDeBarcosDificiles, turnosParaTodos, partidasPorBarco, barcos,cantidadLanzaderas):
		resultados = partidasPorBarco
		while heapDeBarcosDificiles:
			_, barcoActualID = heappop(heapDeBarcosDificiles)
			partidasBarcoActual = self.combinacionesAPartidas(barcoActualID, turnosParaTodos[barcos[barcoActualID]],cantidadLanzaderas)
			for i, partida in enumerate(resultados):
				partidasPosiblesAAppendear = []
				for partidaActual in partidasBarcoActual:
					partidaPosible = simularPartidaConPartidaParcial(partida, partidaActual, cantidadLanzaderas)
					if partidaPosible and partidaPosible not in partidasPosiblesAAppendear: partidasPosiblesAAppendear.append(
						partidaPosible)
				if partidasPosiblesAAppendear: resultados[i] = self.partidaOptima(partidasPosiblesAAppendear)
		return resultados

	def jugarPartidaMatrizFinita(self, resultados, barcos):
		primeraPartida = self.partidaOptima(resultados)
		barcosAtacados = []
		for sublist in primeraPartida:
			if not sublist: continue
			for item in sublist:
				if item != None and item not in barcosAtacados:
					barcosAtacados.append(item)
		if barcosAtacados:
			barcosRemanentes = sorted([b for b in barcos if b.getID() not in barcosAtacados],key=lambda b:-b.getVida())
		else:
			barcosRemanentes = sorted([b for b in barcos if b.getID()],key=lambda b:-b.getVida())
		return primeraPartida, barcosRemanentes


def sortPorBarcoDificilDeMatar(turnosParaTodos):
	heapBarcosDificiles = []
	for barco in turnosParaTodos:
		cantPosiblesCombinaciones = len(turnosParaTodos[barco])
		heappush(heapBarcosDificiles, (cantPosiblesCombinaciones, barco.getID()))
	return heapBarcosDificiles


def simularPartidaConPartidaParcial(partidaParcial, partidaBarcoActual, cantidadLanzaderas):
	for turnoParcial, turnoActual in zip(partidaParcial, partidaBarcoActual):
		if turnoActual and turnoParcial and all([x for x in turnoParcial if x != 0]): return False
	partidaResultado = []
	for turnoParcial, turnoActual in zip(partidaParcial, partidaBarcoActual):
		turnoParcialValido = [x for x in turnoParcial if x != None] if turnoParcial else []
		turnoActualValido = [x for x in turnoActual if x != None] if turnoActual else []
		if len(turnoParcialValido) + len(turnoActualValido) <= cantidadLanzaderas:
			turnoNuevo = turnoParcialValido + turnoActualValido
			partidaResultado.append(turnoNuevo + [None] * (cantidadLanzaderas - len(turnoNuevo)))
	partidaResultado += partidaParcial[len(partidaResultado):]
	partidaResultado += partidaBarcoActual[len(partidaResultado):]
	return partidaResultado


def matarBarcosRemanentes(partida, barcosRemanentes , matriz, cantidadLanzaderas):
	"""De manera greedy, mata a todos los barcos que no pudo matar en una partida con la matriz finita
	Primero llena todas las lanzaderas sin disparar con el primer barco remanente"""
	partidaNueva = []
	for barco in barcosRemanentes:
		vida = barco.getVida()
		id = barco.getID()
		for i, turno in enumerate(partida):
			turnoNuevo = copy(turno)
			if turno and all([x for x in turno if x != 0]): pass
			elif not turno:
				turnoNuevo = [barco.getID()] * (cantidadLanzaderas)
				vida -= cantidadLanzaderas * matriz[id][i]
			else:
				for i, lanzadera in enumerate(turno):
					if lanzadera == None:
						turnoNuevo[i] = id
						vida -= matriz[id][i]
			partidaNueva.append(turnoNuevo)
			if vida <= 0: break
		while (vida > 0):
			partidaNueva.append([barco.getID()] * (cantidadLanzaderas))
			vida -= cantidadLanzaderas * matriz[id][i]
		partidaNueva.append([barco.getID()] * (cantidadLanzaderas))
	return partidaNueva
