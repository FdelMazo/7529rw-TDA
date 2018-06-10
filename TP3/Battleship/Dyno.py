from Jugador import Jugador
from copy import deepcopy


class Dyno(Jugador):
	"""
	Dyno dyno
	"""

	def __init__(self):
		super().__init__('Dyno')

	def turnoDondeMuere(self, barco, matriz):
		"""Devuelve la primera columna en el que se le puede ganar a un barco con la tupla (NroVuelta, Columna)
		Ojo, ambos indices comienzan en 1 en vez de en 0, porque se refieren a vueltas y a columnas (no turnos)"""
		numFila = barco.getID()
		fila = matriz[numFila]
		objetivo = barco.getVida()

		vuelta = 1
		i = 0
		while objetivo > 0:
			for i,elem in enumerate(fila,1):
				objetivo -= elem
				if objetivo <= 0: break
			if objetivo<=0: break
			vuelta+=1
		return (vuelta, i)

	def elegirTargetDelTurno(self, partida):
		barcos, lanzaderas = partida.getBarcosVivos(), partida.getCantidadLanzaderas()
		danioSegunBarco = []
		for barco in reversed(barcos):
			# Reversed para que sea estable el ordenamiento y si tiene dos barcos con la misma vida elija en orden
			x, y = barco.getPosicion()
			danioSegunBarco.append((barco, partida.getDanioCasillero(x, y)))
		danioSegunBarco.sort(key=lambda x: x[1])
		barcoActual = danioSegunBarco[-1]
		vidaActual = barcoActual[0].getVida()
		targets = []
		for i in range(lanzaderas):
			barco, danio = barcoActual
			vidaActual -= danio
			targets.append(barco.getID())
			if vidaActual <=0:
				danioSegunBarco.pop()
				if not danioSegunBarco: break
				barcoActual = danioSegunBarco[-1]
				vidaActual = barcoActual[0].getVida()
		targets += [None] * (lanzaderas - len(targets))
		return targets

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		simulacion = deepcopy(partidaOriginal)
		targetsTotales = []
		matriz = simulacion.getMatriz()

		vuelta, ultimaColumna = max([self.turnoDondeMuere(b, matriz) for b in simulacion.getBarcos()]	)
		cantidadColumnas = len(simulacion.getMatriz()[0])
		cantidadBarcos = len(simulacion.getBarcos())


		cotaTotal = vuelta*cantidadColumnas*cantidadBarcos
		#print(vuelta, cantidadColumnas,cotaTotal)

		while not simulacion.terminada():
			targets = self.elegirTargetDelTurno(simulacion)
			simulacion.setTargetDelTurno(targets)
			simulacion.jugarTurno()
			targetsTotales.append(targets)

		return targetsTotales


# if __name__=='__main__':
# 	from Juego import Juego
# 	from Partida import Partida
#
# 	archivo = 'grilla.coords'
# 	matrizTablero = Juego.ArchivoToMatriz(archivo)
# 	barcos = Juego.ArchivoToBarcos(archivo)
# 	cantidadLanzaderas = 3
#
# 	juego = Juego(matrizTablero, barcos, cantidadLanzaderas)
# 	jugador = Dyno()
# 	partida = Partida(matrizTablero, barcos, cantidadLanzaderas, jugador)
# 	partida.setPosicionesIniciales()
# 	jugador.elegirTargetsDeLaPartida(partida)
