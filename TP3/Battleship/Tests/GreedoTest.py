import unittest
from Greedo import Greedo
from Partida import Partida
from Barco import Barco

class TestUnaLanzadera(unittest.TestCase):
	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleDerribarlo(self):
		greedo = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[100, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleNoDerribarlo(self):
		greedo = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testUnaLanzaderaDosBarcosSacaLaMayorCantidadPosible(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[80, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())
		self.assertTrue(A.getVida() < B.getVida())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuede(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[100, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuedeInvertido(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testUnaLanzaderaDosBarcosDerribaIgualesDerribaAlPrimero(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[100, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

class TestDosLanzaderas(unittest.TestCase):
	def testDosLanzaderasUnBarcoNoSeDisparaABarcoYaMuerto(self):
		greedo = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[100]]
		partida = Partida(matriz, [barco], 2, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		self.assertEqual(targets[0], [0,None])

	def testDosLanzaderasDosBarcosSeMataAUNoSeDaniaAlOtro(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[100],[50]]
		partida = Partida(matriz, [A,B], 2, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		self.assertEqual(targets[0], [0,1])

class TestTresLanzaderas(unittest.TestCase):
	def testTresLanzaderasUnBarcoDerribado(self):
		greedo = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[50, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testTresLanzaderasUnBarcoNoDerribado(self):
		greedo = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribado(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [40, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribadoInvertido(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[10, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoAmbosDerribados(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado(self):
		greedo = Greedo()
		A = Barco(1000)
		B = Barco(1000)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado2(self):
		greedo = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[1, 1000, 30, 10], [2, 1000, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

if __name__ == '__main__':
	unittest.main()