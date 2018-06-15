from Jugador import Jugador
from copy import deepcopy
from copy import copy
from heapq import heappush, heappop
import itertools

import itertools
def psl(l, ts):
	combs = []
	for i in range(len(l)):
		for c in itertools.combinations(l, i):
			if sum(c) >= ts:
				combs.append(list(c))
	return combs
def removeDups(combs):
	newCombs = []
	for c in combs:
		if c in newCombs: continue
		newCombs.append(c)
	return newCombs
def filter(comb, ts):
	for elem in comb[:]:
		indice = comb.index(elem)
		comb.remove(elem)
		if sum(comb) >= ts:
			continue
		comb.insert(indice, elem)
def listaAIndices(lista, listaOriginal):
	listaIndices = []
	for elem in lista:
		indice = listaOriginal.index(elem)
		if indice in listaIndices:
			indice += listaOriginal[indice+1:].index(elem) +1
		listaIndices.append(indice)
	return listaIndices

def subsetMoreThan(lista, objetivo, cantidadLanzaderas, listaOriginal):
	resultados = []
	combs = psl(listaOriginal, objetivo)
	for comb in combs:
		filter(comb, objetivo)
	combs = removeDups(combs)
	for comb in combs:
		indexes = listaAIndices(comb, listaOriginal)
		resultados.append(indexes)
	return resultados

	# listaMultiplicada = copy(lista)
	# if sum(listaMultiplicada[:-1]) >= objetivo:
	# 	return subsetMoreThan(lista[:-1], objetivo, cantidadLanzaderas,listaOriginal)
	# # Dirtiest hack in history: https://stackoverflow.com/a/34238688
	# for elem in listaMultiplicada[:]:
	# 	indice = listaMultiplicada.index(elem)
	# 	listaMultiplicada.remove(elem)
	# 	if sum(listaMultiplicada) >= objetivo:
	# 		lista.pop(indice)
	# 	else: listaMultiplicada.insert(indice, elem)
	# if sum(listaMultiplicada) < objetivo: return
	# resultado = []
	# for elem in lista:
	# 	indice = listaOriginal.index(elem)
	# 	if indice in resultado:
	# 		indice += listaOriginal[indice:].index(elem) +1
	# 	resultado.append(indice)
	# return resultado

def turnosDondePuedeMorir(fila, barco, cantidadLanzaderas):
	combinaciones = subsetMoreThan(fila, barco.getVida(), cantidadLanzaderas, fila)
	combinacionesMatadorasBarco = []
	for combinacion in combinaciones:
		for i, turnos in enumerate(combinacion):
			turnos = [turnos] + [None] * (cantidadLanzaderas - 1)
			combinacion[i] = turnos
		# Crear una lista para cada turno, que sea el turno que recibio, y cantidadLanzaderas-1 de Nones
		if combinacion not in combinacionesMatadorasBarco: combinacionesMatadorasBarco.append(combinacion)
	return combinacionesMatadorasBarco

	# combinacionesMatadorasBarco = []
	# for j in range(len(fila)):
	# 	combinacion = subsetMoreThan(fila[j:], barco.getVida(), cantidadLanzaderas, fila)
	# 	if combinacion and combinacion not in combinacionesMatadorasBarco:
	# 		for i,turnos in enumerate(combinacion):
	# 			turnos = [turnos] + [None] * (cantidadLanzaderas-1)
	# 			combinacion[i] = turnos
	# 		# Crear una lista para cada turno, que sea el turno que recibio, y cantidadLanzaderas-1 de Nones
	# 		combinacionesMatadorasBarco.append(combinacion)
	# return combinacionesMatadorasBarco

def encontrarTodosLosTurnosDondeMuerenTodosLosBarcos(matriz, barcos, cantidadLanzaderas):
	turnosParaTodos = {}
	for y,fila in enumerate(matriz):
		turnosDondeMuere = turnosDondePuedeMorir(fila, barcos[y], cantidadLanzaderas)
		if turnosDondeMuere: turnosParaTodos[barcos[y]] = sorted(turnosDondeMuere)
	return turnosParaTodos

def ordenarPorBarcoMasDificilDeMatar(turnosParaTodos):
	heapBarcosDificiles = []
	for barco in turnosParaTodos:
		cantPosiblesCombinaciones = len(turnosParaTodos[barco])
		heappush(heapBarcosDificiles, (cantPosiblesCombinaciones, barco.getID()))
	return heapBarcosDificiles

def simularPartidaConPartidaParcial(partidaParcial, partidaBarcoActual, cantidadLanzaderas):
	for turnoParcial, turnoActual in zip(partidaParcial, partidaBarcoActual):
		if turnoActual and turnoParcial and all(turnoParcial): return False
	partidaResultado = []
	for turnoParcial, turnoActual in zip(partidaParcial, partidaBarcoActual):
		turnoParcialValido = [x for x in turnoParcial if x!=None] if turnoParcial else []
		turnoActualValido = [x for x in turnoActual if x!=None] if turnoActual else []
		if len(turnoParcialValido) + len(turnoActualValido) <= cantidadLanzaderas:
			turnoNuevo = turnoParcialValido + turnoActualValido
			partidaResultado.append(turnoNuevo+[None]*(cantidadLanzaderas-len(turnoNuevo)))
	partidaResultado += partidaParcial[len(partidaResultado):]
	partidaResultado += partidaBarcoActual[len(partidaResultado):]
	return partidaResultado



class Dyno(Jugador):
	"""
	Dyno dyno
	"""

	def __init__(self):
		super().__init__('Dyno')

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		matriz, barcos, cantidadLanzaderas = partidaOriginal.getMatriz(), partidaOriginal.getBarcosVivos(), partidaOriginal.getCantidadLanzaderas()
		turnosParaTodos = encontrarTodosLosTurnosDondeMuerenTodosLosBarcos(matriz, barcos, cantidadLanzaderas)
		heapDeBarcosDificiles = ordenarPorBarcoMasDificilDeMatar(turnosParaTodos)
		resultados = []
		_, barcoActualID = heappop(heapDeBarcosDificiles)
		#Partida por barco es la forma en la que mato a el barco, con una partida VALIDA (lista de turnos) ej: [[0], [1]] partida validade una lanzadera. [ [1,2], [3,None] ] partida valida de dos
		partidasPorBarco = combinacionDePosibilidadesAPartidas(barcoActualID, turnosParaTodos[barcos[barcoActualID]])
		resultados = partidasPorBarco

		while heapDeBarcosDificiles:
			_, barcoActualID = heappop(heapDeBarcosDificiles)
			barcoActual = barcos[barcoActualID]
			partidasBarcoActual = combinacionDePosibilidadesAPartidas(barcoActualID,
			                                                          turnosParaTodos[barcos[barcoActualID]])
			for i, partida in enumerate(resultados):
				partidasPosiblesAAppendear = []
				for partidaActual in partidasBarcoActual:
					partidaPosible = simularPartidaConPartidaParcial(partida, partidaActual, cantidadLanzaderas)
					if partidaPosible and partidaPosible not in partidasPosiblesAAppendear: partidasPosiblesAAppendear.append(partidaPosible)
				if partidasPosiblesAAppendear: resultados[i] = minimosPuntos(partidasPosiblesAAppendear)
		return minimosPuntos(resultados)

def minimosPuntos(partidas):
	return min(partidas,key=len)

def combinacionDePosibilidadesAPartidas(idBarco, posibilidades):
	partidas = []
	for posibilidad in posibilidades:
		partida = []
		for turno in posibilidad:
			while len(partida) <= turno[0]: partida += [None]
			partida[turno[0]] = [idBarco] + [None] * (len(turno)-1)
		partidas.append(partida)
	return partidas

if __name__=='__main__':
	from Juego import Juego
	from Partida import Partida

	archivo = 'grilla.coords'
	matriz = Juego.ArchivoToMatriz(archivo)
	barcos = Juego.ArchivoToBarcos(archivo)
	cantidadLanzaderas = 3

	juego = Juego(matriz, barcos, cantidadLanzaderas)
	jugador = Dyno()
	partida = Partida(matriz, barcos, cantidadLanzaderas, jugador)
	partida.setPosicionesIniciales()
	targets = jugador.elegirTargetsDeLaPartida(partida)

	print(targets)
	#turnosParaTodos = encontrarTodosLosTurnosDondeMuerenTodosLosBarcos(matriz, barcos, cantidadLanzaderas)
	#heapDeBarcosDificiles = ordenarPorBarcoMasDificilDeMatar(turnosParaTodos)
	#for barco in turnosParaTodos:
	#   artidasPorBarco = combinacionDePosibilidadesAPartidas(barco.getID(), turnosParaTodos[barco])