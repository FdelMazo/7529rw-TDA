class Greedo():
	def __init__(self):
		self.nombre = 'Greedo'

	def turno(self, juego):
		"""Recibe el estado del juego
		Devuelve los targets seleccionados para cada lanzadera"""
		dic = {} #dic = {barco:danioCasillero}
		for barco in juego.getBarcos():
			x, y = barco.getPosicion()
			dic[barco] = juego.getValorCasillero(x, y)
		barcosOrdenados = sorted(dic.items(), key=lambda x: x[1])
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
		return targets