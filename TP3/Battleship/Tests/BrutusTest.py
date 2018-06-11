import unittest
from Brutus import Brutus
from Greedo import Greedo
from Partida import Partida
from Barco import Barco

class TestUnaLanzaderaBrutusSmart(unittest.TestCase):
	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleDerribarlo(self):
		brutus = Brutus()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[100, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleNoDerribarlo(self):
		brutus = Brutus()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testUnaLanzaderaDosBarcosSacaLaMayorCantidadPosible(self):
		brutus = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[80, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())
		self.assertTrue(A.getVida() < B.getVida())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuede(self):
		brutus = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[100, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuedeInvertido(self):
		brutus = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())


class TestTresLanzaderasBrutusSmart(unittest.TestCase):
	def testTresLanzaderasUnBarcoDerribado(self):
		brutus = Brutus()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[50, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testTresLanzaderasUnBarcoNoDerribado(self):
		brutus = Brutus()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribado(self):
		brutus = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [40, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribadoInvertido(self):
		brutus = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[10, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoAmbosDerribados(self):
		brutus = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado(self):
		brutus = Brutus()
		A = Barco(1000)
		B = Barco(1000)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado2(self):
		brutus = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[1, 1000, 30, 10], [2, 1000, 80, 100]]
		partida = Partida(matriz, [A, B], 3, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

class TestCuatroLanzaderasBrutusSmart(unittest.TestCase):
	def testTresLanzaderasDosBarcosNoSeDisparaABarcoDerribado(self):
		greedo = Brutus()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50],[100]]
		partida = Partida(matriz, [A,B], 4, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		self.assertEqual(targets[0], [0,0,0,1])

class TestsDiferenciasBrutus(unittest.TestCase):
	def testGreeedoBrutoEligeElMejorTurnoPosible(self):
		brutus = Brutus()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0,2)
		matriz = [[60],[50],[50]]
		partida = Partida(matriz, [A, B, C], 2, brutus)
		targets = brutus.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(C.estaDerribado())
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testBrutusSmartElijeMismoTurnoQueGreedo(self):
		brutus = Brutus()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0, 2)
		matriz = [[60], [50], [50]]
		partidaBrutus = Partida(matriz, [A, B, C], 2, brutus)
		targetsBrutus = brutus.elegirTargetsDeLaPartida(partidaBrutus)
		greedo = Greedo()
		partidaGreedy = Partida(matriz, [A, B, C], 2, greedo)
		targetsGreedy = greedo.elegirTargetsDeLaPartida(partidaGreedy)
		self.assertEqual(targetsBrutus[:-1],targetsGreedy[:-1])
