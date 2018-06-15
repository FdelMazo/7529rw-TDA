from Jugador import Jugador
from copy import deepcopy
from copy import copy
from heapq import heappush, heappop
import itertools

def subsetMoreThan(lista, objetivo, cantidadLanzaderas, listaOriginal):
	listaMultiplicada = copy(lista)
	if sum(listaMultiplicada[:-1]) >= objetivo:
		return subsetMoreThan(lista[:-1], objetivo, cantidadLanzaderas,listaOriginal)
	# Dirtiest hack in history: https://stackoverflow.com/a/34238688
	for elem in listaMultiplicada[:]:
		indice = listaMultiplicada.index(elem)
		listaMultiplicada.remove(elem)
		if sum(listaMultiplicada) >= objetivo:
			lista.pop(indice)
		else: listaMultiplicada.insert(indice, elem)
	if sum(listaMultiplicada) < objetivo: return
	resultado = []
	for elem in lista:
		indice = listaOriginal.index(elem)
		if indice in resultado:
			indice += listaOriginal[indice:].index(elem) +1
		resultado.append(indice)
	return tuple(resultado)

def turnosDondePuedeMorir(fila, barco, cantidadLanzaderas):
	combinacionesMatadorasBarco = set()
	for j in range(len(fila)):
		combinacion = subsetMoreThan(fila[j:], barco.getVida(), cantidadLanzaderas, fila)
		if combinacion: combinacionesMatadorasBarco.add(combinacion)
	return combinacionesMatadorasBarco

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

def simularPartidaConPartidaParcial(partidaParcial, partidaBarcoActual):
	for i, turno in enumerate(partidaBarcoActual):
		if turno and i<len(partidaParcial) and partidaParcial[i] != None:
			return False
	partidaResultado = []
	for i, turno in enumerate(partidaParcial):
		if i<len(partidaResultado):
			if not partidaResultado[i]: partidaResultado[i] = partidaParcial[i]
		else: partidaResultado.insert(i, turno)
	for i, turno in enumerate(partidaBarcoActual):
		if i<len(partidaResultado):
			if not partidaResultado[i]: partidaResultado[i] = partidaBarcoActual[i]
		else: partidaResultado.insert(i, turno)
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
					partidaPosible = simularPartidaConPartidaParcial(partida, partidaActual)
					if partidaPosible: partidasPosiblesAAppendear.append(partidaPosible)
				resultados[i] = minimosPuntos(partidasPosiblesAAppendear)
		return minimosPuntos(resultados)

def minimosPuntos(partidas):
	return min(partidas,key=len)

def combinacionDePosibilidadesAPartidas(idBarco, posibilidades):
	partidas = []
	for posibilidad in posibilidades:
		partida = []
		for turno in posibilidad:
			while len(partida) <= turno: partida += [None]
			partida[turno] = [idBarco]
		partidas.append(partida)
	return partidas

if __name__=='__main__':
	from Juego import Juego
	from Partida import Partida

	archivo = 'grilla.coords'
	matriz = Juego.ArchivoToMatriz(archivo)
	barcos = Juego.ArchivoToBarcos(archivo)
	cantidadLanzaderas = 2

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