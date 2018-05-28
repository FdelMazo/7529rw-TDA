from RedDeTransporte import *


ARCHIVO = redsecreta.map


def cargarArchivo():
	red = RedDeTransporte()
	
	with open(ARCHIVO) as file:
		
		lineas = file.readlines()
		
		for linea in lineas:
		
			numOrigen, numDestino, peso = linea.spit(' ')
			red.agregarArista(numOrigen, numDestino, peso)
	
	return red

