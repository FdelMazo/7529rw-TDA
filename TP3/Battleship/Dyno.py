from Jugador import Jugador
from copy import deepcopy
from heapq import heappush, heappop
import itertools

def subsetMoreThan(lista, objetivo, cantidadLanzaderas, listaOriginal):
	listaMultiplicada = [i * cantidadLanzaderas for i in lista]
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

def ordenarPorBarcoMasDificilDeMatar(matriz, barcos, cantidadLanzaderas):
	turnosParaTodos = encontrarTodosLosTurnosDondeMuerenTodosLosBarcos(matriz, barcos, cantidadLanzaderas)
	heapBarcosDificiles = []
	for barco in turnosParaTodos.keys():
		cantPosiblesCombinaciones = len(turnosParaTodos[barco])
		heappush(heapBarcosDificiles, (cantPosiblesCombinaciones, barco.getID()))
	return heapBarcosDificiles


class Dyno(Jugador):
	"""
	Dyno dyno
	"""

	def __init__(self):
		super().__init__('Dyno')

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		pass


if __name__=='__main__':
	from Juego import Juego
	from Partida import Partida

	archivo = 'grilla.coords'
	matrizTablero = Juego.ArchivoToMatriz(archivo)
	barcos = Juego.ArchivoToBarcos(archivo)
	cantidadLanzaderas = 1

	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
	jugador = Dyno()
	partida = Partida(matrizTablero, barcos, cantidadLanzaderas, jugador)
	partida.setPosicionesIniciales()
	heap = ordenarPorBarcoMasDificilDeMatar(matrizTablero, barcos, cantidadLanzaderas)
	while heap:
		cantPosiblesCombinaciones, id = heappop(heap)
		print("Hay {} chances de matar al {}".format(cantPosiblesCombinaciones, barcos[id]))
	# jugador.elegirTargetsDeLaPartida(partida)
