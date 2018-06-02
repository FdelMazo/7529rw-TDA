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