import unittest
from Tablero import *

class TestMoverBarco(unittest.TestCase):
    def testMoverBarco(self):
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        matriz = [[10, 30, 40, 50]]
        tablero = Tablero(matriz, barcos, 0)
        tablero.avanzarBarcos()
        self.assertEqual(barco.getPosicion(), (0,1))

class TestBarcoVuelveAlInicio(unittest.TestCase):
    def testUnBarcoPosicionadoAlFinalDeLaFilaVuelveAlInicio(self):
        barco = Barco(100)
        barco.setPosicion(3, 0)
        barcos = [barco]
        matriz = [[10, 30, 40, 50]]
        tablero = Tablero(matriz, barcos, 0)
        tablero.avanzarBarcos()
        self.assertEqual(barco.getPosicion(), (0,0))

class TestDanioCorrectoEnElCasillero(unittest.TestCase):
    def testDanioCorrecto(self):
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        matriz = [[1, 2, 3], [4, 5, 6]]
        tablero = Tablero(matriz, barcos, 1)
        self.assertEqual(tablero.getValorCasillero(2, 1), 6)
