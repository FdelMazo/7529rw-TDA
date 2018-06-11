import unittest

from Partida import Partida
from Barco import Barco


class TestBarco(unittest.TestCase):
	def testMoverBarco(self):
		barco = Barco(100)
		barco.setPosicion(0, 0)
		barcos = [barco]
		matriz = [[10, 30, 40, 50]]
		partida = Partida(matriz, barcos, 0, None)
		partida.avanzarBarcos()
		self.assertEqual(barco.getPosicion(), (1, 0))

	def testUnBarcoPosicionadoAlFinalDeLaFilaVuelveAlInicio(self):
		barco = Barco(100)
		barco.setPosicion(3, 0)
		barcos = [barco]
		matriz = [[10, 30, 40, 50]]
		partida = Partida(matriz, barcos, 0, None)
		partida.avanzarBarcos()
		self.assertEqual(barco.getPosicion(), (0, 0))

	def testSetPosicionesIniciales(self):
		barco1 = Barco(100)
		barco2 = Barco(100)
		barcos = [barco1, barco2]
		partida = Partida([[0, 0], [0, 0]], barcos, 0, None)
		partida.setPosicionesIniciales()
		for i,b in enumerate(barcos):
			self.assertEqual(b.getPosicion(),(0,i))

	def testBarcosVivos(self):
		barco1 = Barco(100)
		barco2 = Barco(100)
		barcos = [barco1, barco2]
		partida = Partida([[0, 0], [0, 0]], barcos, 0, None)
		barco1.recibirDanio(100)
		self.assertEqual(partida.getBarcosVivos(), [barco2])
		barco2.recibirDanio(100)
		self.assertFalse(partida.getBarcosVivos())

class TestDanioCasilleros(unittest.TestCase):
	def testDanioCorrecto(self):
		barco = Barco(100)
		barco.setPosicion(2, 1)
		barcos = [barco]
		matriz = [[1, 2, 3], [4, 5, 6]]
		partida = Partida(matriz, barcos, 1, None)
		self.assertEqual(partida.getDanioCasillero(2, 1), 6)
		self.assertEqual(partida.getDanioCasillero(*barco.getPosicion()), 6)


class TestPartidaTerminada(unittest.TestCase):
	def testPartidaTerminada(self):
		barco1 = Barco(100)
		barco2 = Barco(100)
		barco1.recibirDanio(100)
		barco2.recibirDanio(100)
		barcos = [barco1, barco2]
		partida = Partida([[0, 0], [0, 0]], barcos, 0, None)
		self.assertTrue(partida.terminada())
		self.assertFalse(partida.getBarcosVivos())
