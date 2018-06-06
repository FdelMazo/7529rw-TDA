from RedDeTransporte import *
from FlujoMaximo import *
from heapq import heappop, nlargest

ARCHIVO = "redsecreta.map"


def cargarArchivoSabotage(archivo = ARCHIVO):
	
	red = RedDeTransporte()
	
	with open(archivo) as file:
		lineas = file.readlines()
		
		for linea in lineas:	
			numOrigen, numDestino, peso = linea.split(' ')
			red.agregarArista(int(numOrigen), int(numDestino), int(peso))
	
	return red


def protegerAristas(aristasAProteger, cantidadDeVigilancias, aristasProtegidas):
	
	for a in aristasAProteger:
		if (cantidadDeVigilancias == 0):
			break
		
		aristasProtegidas.append(a)
		cantidadDeVigilancias -= 1
	
	return cantidadDeVigilancias


def proteger2Aristas(red):

	cantidadDeVigilancias = 2
	aristasProtegidas = []
	unFlujoMaximo, cuellosDeBotella, unosCaminos =  FordFulkerson(red)
	aristasDeCorte = red.obtenerAristasDeCorte()
	
	for a in aristasDeCorte:
		aristaIgual = obtenerAristaIgualIncluida(a, cuellosDeBotella)
		if aristaIgual:
			cuellosDeBotella.remove(a)
	
	cuellosDeBotella.sort(reverse=True)

	cantidadDeVigilancias = protegerAristas(aristasDeCorte, cantidadDeVigilancias, aristasProtegidas)
	cantidadDeVigilancias = protegerAristas(cuellosDeBotella, cantidadDeVigilancias, aristasProtegidas)
	return aristasProtegidas

