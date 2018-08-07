from RedDeTransporte import *
from FlujoMaximo import *
from AntiSabotaje import *

def PlanVigilancia():
	red = cargarArchivoAntiSabotaje()
	print("Red de información de C.O.N.T.R.O.L.\n" + str(red))
	aristasAProteger = proteger2Aristas(red)
	print("Flujo máximo de la red: " + str(flujoMaximo(red)) )
	
	for a in aristasAProteger:
		print("\nSe protege la arista: " + str(a).rstrip())
		numOrigen = a.obtenerOrigen().obtenerNumero()
		numDestino = a.obtenerDestino().obtenerNumero()
		peso = a.obtenerPeso()
		identificador = a.obtenerId()
		red.borrarArista(numOrigen, numDestino, identificador)
		print("Flujo máximo de la red sin " + str(a).rstrip() + ": "+ str(flujoMaximo(red)).rstrip() )
		red.agregarArista(numOrigen, numDestino, peso, identificador)
	
PlanVigilancia()
