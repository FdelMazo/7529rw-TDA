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
        barco.setPosicion(0, 3)
        barcos = [barco]
        matriz = [[10, 30, 40, 50]]
        tablero = Tablero(matriz, barcos, 0)
        tablero.avanzarBarcos()
        self.assertEqual(barco.getPosicion(), (0,0))
