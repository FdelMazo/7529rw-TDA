import unittest

from Partida import Partida
from Barco import Barco

class TestMoverBarco(unittest.TestCase):
    def testMoverBarco(self):
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        matriz = [[10, 30, 40, 50]]
        juego = Partida(matriz, barcos, 0, None)
        juego.avanzarBarcos()
        self.assertEqual(barco.getPosicion(), (1,0))

class TestBarcoVuelveAlInicio(unittest.TestCase):
    def testUnBarcoPosicionadoAlFinalDeLaFilaVuelveAlInicio(self):
        barco = Barco(100)
        barco.setPosicion(3, 0)
        barcos = [barco]
        matriz = [[10, 30, 40, 50]]
        juego = Partida(matriz, barcos, 0, None)
        juego.avanzarBarcos()
        self.assertEqual(barco.getPosicion(), (0,0))

class TestDanioCorrectoEnElCasillero(unittest.TestCase):
    def testDanioCorrecto(self):
        barco = Barco(100)
        barco.setPosicion(0, 0)
        barcos = [barco]
        matriz = [[1, 2, 3], [4, 5, 6]]
        juego = Partida(matriz, barcos, 1, None)
        self.assertEqual(juego.getDanioCasillero(2, 1), 6)

if __name__ == '__main__':
	unittest.main()