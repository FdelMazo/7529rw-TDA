import unittest
from Greedo import *

class TestDerribarUnBarcoCon1Lanzadera(unittest.TestCase):
    def testBarcoDerribado(self):
        matriz = [[100, 40, 30, 10]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        tablero = Tablero(matriz, barcos, 1)
        GreedoTurno(tablero, matriz, barcos, 1)
        self.assertTrue(barco.estaDerribado())

    def testBarcoNoDerribado(self):
        matriz = [[10, 40, 30, 50]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        tablero = Tablero(matriz, barcos, 1)
        GreedoTurno(tablero, matriz, barcos, 1)
        self.assertFalse(barco.estaDerribado())


class TestDerribarUnBarcoCon3Lanzaderas(unittest.TestCase):
    def testBarcoDerribado(self):
        matriz = [[50, 40, 30, 10]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        tablero = Tablero(matriz, barcos, 3)
        GreedoTurno(tablero, matriz, barcos, 3)
        self.assertTrue(barco.estaDerribado())

    def testBarcoNoDerribado(self):
        matriz = [[10, 40, 30, 50]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        tablero = Tablero(matriz, barcos, 3)
        GreedoTurno(tablero, matriz, barcos, 3)
        self.assertFalse(barco.estaDerribado())

class TestDerribarDosBarcosCon1Lanzadera(unittest.TestCase):
    def testADerribadoBSinDerribar(self):
        matriz = [[100, 40, 30, 10], [40, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(1, 0)
        barcos = [A, B]
        tablero = Tablero(matriz, barcos, 1)
        GreedoTurno(tablero, matriz, barcos, 1)
        self.assertTrue(A.estaDerribado() and not B.estaDerribado())

    def testBDerribadoASinDerribar(self):
        matriz = [[10, 40, 30, 10], [400, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(1, 0)
        barcos = [A, B]
        tablero = Tablero(matriz, barcos, 1)
        GreedoTurno(tablero, matriz, barcos, 1)
        self.assertTrue(not A.estaDerribado() and B.estaDerribado())

class TestDerribarDosBarcosCon3Lanzadera(unittest.TestCase):
    def testADerribadoBSinDerribar(self):
        matriz = [[50, 40, 30, 10], [40, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(1, 0)
        barcos = [A, B]
        tablero = Tablero(matriz, barcos, 3)
        GreedoTurno(tablero, matriz, barcos, 3)
        self.assertTrue(A.estaDerribado() and not B.estaDerribado())

    def testBDerribadoASinDerribar(self):
        matriz = [[10, 40, 30, 10], [50, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(1, 0)
        barcos = [A, B]
        tablero = Tablero(matriz, barcos, 3)
        GreedoTurno(tablero, matriz, barcos, 3)
        self.assertTrue(not A.estaDerribado() and B.estaDerribado())

    def testADerribadoADerribado(self):
        matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(1, 0)
        barcos = [A, B]
        tablero = Tablero(matriz, barcos, 3)
        GreedoTurno(tablero, matriz, barcos, 3)
        self.assertTrue(A.estaDerribado() and B.estaDerribado())

    def ASinDerribarBSinDerribar(self):
        matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
        A = Barco(1000)
        B = Barco(1000)
        A.setPosicion(0, 0)
        B.setPosicion(1, 0)
        barcos = [A, B]
        tablero = Tablero(matriz, barcos, 3)
        GreedoTurno(tablero, matriz, barcos, 3)
        self.assertFalse(A.estaDerribado() and B.estaDerribado())
