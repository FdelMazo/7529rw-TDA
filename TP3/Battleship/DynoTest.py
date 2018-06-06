import unittest
from Dyno import *
from Juego import Juego
from Barco import Barco

class TestDerribarUnBarcoCon1Lanzadera(unittest.TestCase):
    def testBarcoDerribado(self):
        dyno = Dyno()
        matriz = [[100, 40, 30, 10]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        juego = Juego(matriz, [barco], 1)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(barco.estaDerribado())

    def testBarcoNoDerribado(self):
        dyno = Dyno()
        matriz = [[10, 40, 30, 50]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        juego = Juego(matriz, [barco], 1)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertFalse(barco.estaDerribado())


class TestDerribarUnBarcoCon3Lanzaderas(unittest.TestCase):
    def testBarcoDerribado(self):
        dyno = Dyno()
        matriz = [[50, 40, 30, 10]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        juego = Juego(matriz, [barco], 3)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(barco.estaDerribado())

    def testBarcoNoDerribado(self):
        dyno = Dyno()
        matriz = [[10, 40, 30, 50]]
        barco = Barco(100)
        barco.setPosicion(0, 0)
        juego = Juego(matriz, [barco], 3)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertFalse(barco.estaDerribado())

class TestDerribarDosBarcosCon1Lanzadera(unittest.TestCase):
    def testADerribadoBSinDerribar(self):
        dyno = Dyno()
        matriz = [[100, 40, 30, 10], [40, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(0, 1)
        juego = Juego(matriz, [A,B], 1)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(A.estaDerribado() and not B.estaDerribado())

    def testBDerribadoASinDerribar(self):
        dyno = Dyno()
        matriz = [[10, 40, 30, 10], [400, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(0, 1)
        juego = Juego(matriz, [A,B], 1)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(not A.estaDerribado() and B.estaDerribado())

class TestDerribarDosBarcosCon3Lanzadera(unittest.TestCase):
    def testADerribadoBSinDerribar(self):
        dyno = Dyno()
        matriz = [[50, 40, 30, 10], [40, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(0, 1)
        juego = Juego(matriz, [A,B], 3)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(A.estaDerribado() and not B.estaDerribado())

    def testBDerribadoASinDerribar(self):
        dyno = Dyno()
        matriz = [[10, 40, 30, 10], [50, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(0, 1)
        juego = Juego(matriz, [A,B], 3)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(not A.estaDerribado() and B.estaDerribado())

    def testADerribadoADerribado(self):
        dyno = Dyno()
        matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(0, 1)
        juego = Juego(matriz, [A,B], 3)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(A.estaDerribado() and B.estaDerribado())

    def testASinDerribarBSinDerribar1(self):
        dyno = Dyno()
        matriz = [[50, 40, 30, 10], [100, 30, 80, 100]]
        A = Barco(1000)
        B = Barco(1000)
        A.setPosicion(0, 0)
        B.setPosicion(0, 1)
        juego = Juego(matriz, [A,B], 3)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertFalse(A.estaDerribado() and B.estaDerribado())

    def testASinDerribarBDerribado2(self):
        dyno = Dyno()
        matriz = [[1, 1000, 30, 10], [2, 1000, 80, 100]]
        A = Barco(100)
        B = Barco(100)
        A.setPosicion(0, 0)
        B.setPosicion(1, 0)
        juego = Juego(matriz, [A,B], 3)
        juego.setJugador(dyno)
        juego.jugar()
        juego.avanzarTurno()
        self.assertTrue(not A.estaDerribado() and B.estaDerribado())

if __name__ == '__main__':
	unittest.main()