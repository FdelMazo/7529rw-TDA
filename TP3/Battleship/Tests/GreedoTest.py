import unittest
from Greedo import Greedo
from GreedoNaive import GreedoNaive
from Partida import Partida
from Barco import Barco

class TestUnaLanzaderaGreedoSmart(unittest.TestCase):
	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleDerribarlo(self):
		greedobruto = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[100, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testUnaLanzaderaUnBarcoUnicaOpcionPosibleNoDerribarlo(self):
		greedobruto = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 1, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testUnaLanzaderaDosBarcosSacaLaMayorCantidadPosible(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[80, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())
		self.assertTrue(A.getVida() < B.getVida())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuede(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[100, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testUnaLanzaderaDosBarcosDerribaAlQuePuedeInvertido(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0,1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testUnaLanzaderaDosBarcosDerribaIgualesDerribaAlPrimero(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[100, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A,B], 1, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

class TestDosLanzaderasGreedoSmart(unittest.TestCase):
	def testDosLanzaderasUnBarcoNoSeDisparaABarcoYaMuerto(self):
		greedo = GreedoNaive()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[100]]
		partida = Partida(matriz, [barco], 2, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		self.assertEqual(targets[0], [0,None])

	def testDosLanzaderasDosBarcosSeMataAUNoSeDaniaAlOtro(self):
		greedo = GreedoNaive()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[100],[50]]
		partida = Partida(matriz, [A,B], 2, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		self.assertEqual(targets[0], [0,1])

class TestTresLanzaderasGreedoSmart(unittest.TestCase):
	def testTresLanzaderasUnBarcoDerribado(self):
		greedobruto = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[50, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(barco.estaDerribado())

	def testTresLanzaderasUnBarcoNoDerribado(self):
		greedobruto = Greedo()
		barco = Barco(100)
		barco.setPosicion(0, 0)
		matriz = [[10, 40, 30, 10]]
		partida = Partida(matriz, [barco], 3, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(barco.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribado(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [40, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoUnoDerribadoInvertido(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[10, 40, 30, 10], [50, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoAmbosDerribados(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado(self):
		greedobruto = Greedo()
		A = Barco(1000)
		B = Barco(1000)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testTresLanzaderasDosBarcoNingunoDerribado2(self):
		greedobruto = Greedo()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[1, 1000, 30, 10], [2, 1000, 80, 100]]
		partida = Partida(matriz, [A, B], 3, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

class TestCuatroLanzaderasGreedoSmart(unittest.TestCase):
	def testTresLanzaderasDosBarcosNoSeDisparaABarcoDerribado(self):
		greedo = GreedoNaive()
		A = Barco(100)
		B = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[50],[100]]
		partida = Partida(matriz, [A,B], 4, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partida)
		self.assertEqual(targets[0], [1,0,0,None])

class TestsDiferenciasGreedoNaive(unittest.TestCase):
	def testGreeedoBrutoEligeElMejorTurnoPosible(self):
		greedobruto = Greedo()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0,2)
		matriz = [[60],[50],[50]]
		partida = Partida(matriz, [A, B, C], 2, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(C.estaDerribado())
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testGreedoSmartElijeMejorTurnoQueGreedo(self):
		greedobruto = Greedo()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0, 2)
		matriz = [[60], [50], [50]]
		partida = Partida(matriz, [A, B, C], 2, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertTrue(C.estaDerribado())
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

		greedo = GreedoNaive()
		A = Barco(300)
		B = Barco(200)
		C = Barco(100)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		C.setPosicion(0, 2)
		partidaG = Partida(matriz, [A, B, C], 2, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partidaG)
		partidaG.setTargetDelTurno(targets[0])
		partidaG.jugarTurno()
		self.assertFalse(C.estaDerribado())
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())

	def testGreedoSmartElijeMejorTurnoQueGreedo2(self):
		greedobruto = Greedo()
		A = Barco(700)
		B = Barco(260)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		matriz = [[300], [280]]
		partida = Partida(matriz, [A, B], 2, greedobruto)
		targets = greedobruto.elegirTargetsDeLaPartida(partida)
		partida.setTargetDelTurno(targets[0])
		partida.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertTrue(B.estaDerribado())

		greedo = GreedoNaive()
		A = Barco(700)
		B = Barco(260)
		A.setPosicion(0, 0)
		B.setPosicion(0, 1)
		partidaG = Partida(matriz, [A, B], 2, greedo)
		targets = greedo.elegirTargetsDeLaPartida(partidaG)
		partidaG.setTargetDelTurno(targets[0])
		partidaG.jugarTurno()
		self.assertFalse(A.estaDerribado())
		self.assertFalse(B.estaDerribado())
