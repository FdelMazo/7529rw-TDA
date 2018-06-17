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

		turnosParaTodos = {}
		for id, fila in enumerate(matriz):
			turnosDondeMuere = self.combinacionesMatadoras(fila, barcos[id].getVida())
			if turnosDondeMuere: turnosParaTodos[barcos[id]] = sorted(turnosDondeMuere)

		heapDeBarcosDificiles = self.sortPorBarcoDificilDeMatar(turnosParaTodos)
		_, barcoMasDificil = heappop(heapDeBarcosDificiles)
		partidasPrimerBarco = self.combinacionesAPartidas(barcoMasDificil, turnosParaTodos[barcos[barcoMasDificil]],cantidadLanzaderas)
		partidaAJugar = self.definirPartidaAJugar(heapDeBarcosDificiles, turnosParaTodos, partidasPrimerBarco, barcos,cantidadLanzaderas)

		partida, barcosRemanentes = self.jugarPartidaMatrizFinita(partidaAJugar, barcos)
		if barcosRemanentes: partida = self.matarBarcosRemanentes(partida, barcosRemanentes, matriz, cantidadLanzaderas)
		return partida

	def definirPartidaAJugar(self, heapDeBarcosDificiles, turnosParaTodos, partidasPrimerBarco, barcos, cantidadLanzaderas):
		"""Recorre todos los barcos del mas dificil al mas facil de matar.
		Para cada barco juega la partida anterior pero agregandole un barco
		De todas las posibles partidas, se queda con la optima
		Al final, devuelve la partida optima de todas las partidas optimas posibles
		"""
		partidas = partidasPrimerBarco
		while heapDeBarcosDificiles:
			_, proximoBarco = heappop(heapDeBarcosDificiles)
			partidasProximoBarco = self.combinacionesAPartidas(proximoBarco, turnosParaTodos[barcos[proximoBarco]],cantidadLanzaderas)
			for i, partida in enumerate(partidas):
				partidasPosibles = []
				for partidaActual in partidasProximoBarco:
					partidaPosible = self.jugarPartidaNueva(partida, partidaActual, cantidadLanzaderas)
					if not partidaPosible: continue
					if partidaPosible not in partidasPosibles: partidasPosibles.append(partidaPosible)
				if partidasPosibles: partidas[i] = self.partidaOptima(partidasPosibles)
		return self.partidaOptima(partidas)

	def partidaOptima(self, partidas):
		"""La partida optima de una lista de partidas es la mas 'ajustada', es decir, la que mas dispara y gana lo antes posible
		De esta forma se logra que no se extienda la partida dejandola llena de lanzaderas que no disparan"""
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

	def jugarPartidaMatrizFinita(self, resultados, barcos):
		barcosAtacados = []
		for sublist in resultados:
			if not sublist: continue
			for item in sublist:
				if item != None and item not in barcosAtacados:
					barcosAtacados.append(item)
		if barcosAtacados:
			barcosRemanentes = sorted([b for b in barcos if b.getID() not in barcosAtacados],key=lambda b:-b.getVida())
		else:
			barcosRemanentes = sorted([b for b in barcos if b.getID()],key=lambda b:-b.getVida())
		return resultados, barcosRemanentes

	def jugarPartidaNueva(self, partidaVieja, partidaAgregada, cantidadLanzaderas):
		"""Teniendo en cuenta una partida parcialmente jugada para un barco (partidaVieja), agrega una segunda partida (partidaAgregada) que mata al nuevo barco"""
		for turnoParcial, turnoActual in zip(partidaVieja, partidaAgregada):
			# Si no son compatibles las partidas, la descarta
			if turnoActual and turnoParcial and all([x for x in turnoParcial if x != 0]): return False
		partidaNueva = []
		for turnoParcial, turnoActual in zip(partidaVieja, partidaAgregada):
			turnoParcialValido = [x for x in turnoParcial if x != None] if turnoParcial else []
			turnoActualValido = [x for x in turnoActual if x != None] if turnoActual else []
			if len(turnoParcialValido) + len(turnoActualValido) <= cantidadLanzaderas:
				turnoNuevo = turnoParcialValido + turnoActualValido
				partidaNueva.append(turnoNuevo + [None] * (cantidadLanzaderas - len(turnoNuevo)))
		partidaNueva += partidaVieja[len(partidaNueva):]
		partidaNueva += partidaAgregada[len(partidaNueva):]
		return partidaNueva

	def sortPorBarcoDificilDeMatar(self,turnosParaTodos):
		"""El barco mas dificil de matar es el que menos partidas que lo mate tenga"""
		heapBarcosDificiles = []
		for barco in turnosParaTodos:
			cantidadPartidasPosiblesQueLoMatan = len(turnosParaTodos[barco])
			heappush(heapBarcosDificiles, (cantidadPartidasPosiblesQueLoMatan, barco.getID()))
		return heapBarcosDificiles

	def matarBarcosRemanentes(self,partida, barcosRemanentes , matriz, cantidadLanzaderas):
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
