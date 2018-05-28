from RedDeTransporte import *


ARCHIVO = "redsecreta.map"


def cargarArchivoSabotage(archivo = ARCHIVO):
	red = RedDeTransporte()
	
	with open(archivo) as file:
		
		lineas = file.readlines()
		
		for linea in lineas:
		
			numOrigen, numDestino, peso = linea.split(' ')
			red.agregarArista(int(numOrigen), int(numDestino), int(peso))
	
	return red
