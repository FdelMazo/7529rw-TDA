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

def ordenarPorBarcoMasDificilDeMatar(turnosParaTodos):
	heapBarcosDificiles = []
	for barco in turnosParaTodos:
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
	cantidadLanzaderas = 1

	juego = Juego(matriz, barcos, cantidadLanzaderas)
	jugador = Dyno()
	partida = Partida(matriz, barcos, cantidadLanzaderas, jugador)
	partida.setPosicionesIniciales()
	turnosParaTodos = encontrarTodosLosTurnosDondeMuerenTodosLosBarcos(matriz, barcos, cantidadLanzaderas)
	heapDeBarcosDificiles = ordenarPorBarcoMasDificilDeMatar(turnosParaTodos)
	for barco in turnosParaTodos:
		partidasPorBarco = combinacionDePosibilidadesAPartidas(barco.getID(), turnosParaTodos[barco])
		print("Las distintas partidas para ganarle a {} son: {}".format(barco, partidasPorBarco))