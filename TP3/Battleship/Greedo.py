from Jugador import Jugador

class Greedo(Jugador):
	def __init__(self):
		super().__init__('Greedo')

	def elegirTargets(self, juego):
		"""Recibe el estado del juego, NO LO MODIFICA (dummy/copy)
		Devuelve una lista de filas de barcos a los que ataca cada lanzadera"""
		danioSegunBarco = {}
		for barco in juego.getBarcos():
			x, y = barco.getPosicion()
			danioSegunBarco[barco] = juego.getDanioCasillero(x, y)
		barcosOrdenados = sorted(danioSegunBarco.items(), key=lambda x: x[1])
		barcosDisponibles = len(barcosOrdenados)
		barcoActual = barcosOrdenados[barcosDisponibles - 1]
		targets = []
		for i in range(juego.getCantidadLanzaderas()):
			barco, danio = barcoActual
			dummyVida = barco.getVida()
			dummyVida -= danio
			targets.append(barco)
			if dummyVida <= 0:
				barcosDisponibles -= 1
				if barcosDisponibles == 0:
					break
				barcoActual = barcosOrdenados[barcosDisponibles-1]
		targets += [None] * (juego.getCantidadLanzaderas() - len(targets))
		return [t.getPosicion()[1] if t else None for t in targets ]