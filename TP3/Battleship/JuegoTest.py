import unittest

from Juego import Juego
from Barco import Barco

class TestMoverBarco(unittest.TestCase):
    def testMoverBarco(self):
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        matriz = [[10, 30, 40, 50]]
        juego = Juego(matriz, barcos, 0)
        juego.avanzarBarcos()
        self.assertEqual(barco.getPosicion(), (1,0))

class TestBarcoVuelveAlInicio(unittest.TestCase):
    def testUnBarcoPosicionadoAlFinalDeLaFilaVuelveAlInicio(self):
        barco = Barco(100)
        barco.setPosicion(3, 0)
        barcos = [barco]
        matriz = [[10, 30, 40, 50]]
        juego = Juego(matriz, barcos, 0)
        juego.avanzarBarcos()
        self.assertEqual(barco.getPosicion(), (0,0))

class TestDanioCorrectoEnElCasillero(unittest.TestCase):
    def testDanioCorrecto(self):
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        matriz = [[1, 2, 3], [4, 5, 6]]
        juego = Juego(matriz, barcos, 1)
        self.assertEqual(juego.getValorCasillero(2, 1), 6)

if __name__ == '__main__':
	unittest.main()