from RedDeTransporte import *
from FlujoMaximo import *
from heapq import heapify, heappop

ARCHIVO = "redsecreta.map"


def cargarArchivoSabotage(archivo = ARCHIVO):
	red = RedDeTransporte()
	
	with open(archivo) as file:
		
		lineas = file.readlines()
		
		for linea in lineas:
		
			numOrigen, numDestino, peso = linea.split(' ')
			red.agregarArista(int(numOrigen), int(numDestino), int(peso))
	
	return red


def obtenerAristasDeCorte(caminosReales):
	
	caminosRealesAux = caminosReales
	coincidencias = 0
	cantCaminos = len(caminosReales)
	aristasDeCorte = []
	
	for c in caminosReales:
		for a in c:
			for cAux in caminosRealesAux:
				if a in cAux:
					coincidencias +=1 
			
			if coincidencias == cantCaminos:
				aristasDeCorte.append(a)
	
	aristasDeCorteOrdenadas = []
	heapify(aristasDeCorte)
	while aristasDeCorte:
		aristasDeCorteOrdenadas.append(heappop(aristasDeCorte))
	
	return aristasDeCorte


def proteger2Aristas(red):

	cantidadDeVigilancias = 2
	aristasProtegidas = []
	flujoMaximo, cuellosDeBotella, caminosReales =  FordFulkerson(red)
	
	aristasDeCorte =  obtenerAristasDeCorte(caminosReales)	
	
	for a in aristasDeCorte:
		aristasProtegidas.append(a)
		cantidadDeVigilancias-=1
		
		if (cantidadDeVigilancias == 0):
			break
		
	for a in cuellosDeBotella:
		aristasProtegidas.append(a)
		cantidadDeVigilancias-=1
			
		if (cantidadDeVigilancias == 0):
			break
	
	return aristasProtegidas
	
