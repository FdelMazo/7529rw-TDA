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

		turnosParaTodos = self.comoMatarBarcos(matriz, barcos, cantidadLanzaderas)
		heapDeBarcosDificiles = sortPorBarcoDificilDeMatar(turnosParaTodos)
		_, barcoActualID = heappop(heapDeBarcosDificiles)
		partidasPorBarco = self.combinacionesAPartidas(barcoActualID, turnosParaTodos[barcos[barcoActualID]],cantidadLanzaderas)

		resultados = self.definirPartidaAJugar(heapDeBarcosDificiles, turnosParaTodos, partidasPorBarco, barcos,cantidadLanzaderas)

		primeraPartida, barcosRemanentes = self.jugarPrimeraPartida(resultados, barcos)
		if not barcosRemanentes: return primeraPartida

		segundaPartida = jugarSegundaPartida(barcosRemanentes, primeraPartida, matriz, cantidadLanzaderas)
		return segundaPartida

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
			resultados.append(listaIndices)
		return resultados

	def combinacionesParaBarco(self, fila, barco, cantidadLanzaderas):
		combinaciones = self.combinacionesMatadoras(fila, barco.getVida())
		combinacionesMatadorasBarco = []
		for combinacion in combinaciones:
			if combinacion not in combinacionesMatadorasBarco: combinacionesMatadorasBarco.append(combinacion)
		return combinacionesMatadorasBarco

	def comoMatarBarcos(self, matriz, barcos, cantidadLanzaderas):
		turnosParaTodos = {}
		for y, fila in enumerate(matriz):
			turnosDondeMuere = self.combinacionesParaBarco(fila, barcos[y], cantidadLanzaderas)
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

	def jugarPrimeraPartida(self, resultados, barcos):
		primeraPartida = self.partidaOptima(resultados)
		barcosRemanentes = None
		barcosDePrimeraPartida = []
		for sublist in primeraPartida:
			if not sublist: continue
			for item in sublist:
				if item != None and item not in barcosDePrimeraPartida:
					barcosDePrimeraPartida.append(item)
		if barcosDePrimeraPartida:
			barcosRemanentes = [b for b in barcos if b.getID() not in barcosDePrimeraPartida]
		else:
			barcosRemanentes = [b for b in barcos if b.getID()]
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


def jugarSegundaPartida(barcosRemanentes, primeraPartida, matriz, cantidadLanzaderas):
	segundaPartida = []
	for b in barcosRemanentes:
		vida = b.getVida()
		id = b.getID()
		for i, turno in enumerate(primeraPartida):
			turnoNuevo = copy(turno)
			if turno and all([x for x in turno if x != 0]):
				pass
			elif not turno:
				turnoNuevo = [b.getID()] * (cantidadLanzaderas)
				vida -= cantidadLanzaderas * matriz[id][i - 1]
			else:
				for i, lanzadera in enumerate(turno):
					if lanzadera == None:
						turnoNuevo[i] = b.getID()
						vida -= matriz[id][i - 1]
			segundaPartida.append(turnoNuevo)
		while (vida > 0):
			segundaPartida.append([b.getID()] * (cantidadLanzaderas))
			vida -= cantidadLanzaderas * matriz[id][i-1]
		segundaPartida.append([b.getID()] * (cantidadLanzaderas))
	return segundaPartida
