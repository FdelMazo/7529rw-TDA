import unittest
from Dino import *
from Partida import Partida
from Barco import Barco

class TestDevolverTuplasOrdenadasConUnaSolaTupla(unittest.TestCase):
    def testDevolverTuplasOrdenadasConUnaSolaTupla(self):
        dino = Dino()
        barco = Barco(100)
        barco.setPosicion(0, 0)
        matriz = [[100, 40, 60, 10]]
        partida = Partida(matriz, [barco], 1, dino)
        tuplas = dino.devolverTuplasOrdenadasDanioTurnoBarco(partida)
        self.assertEqual(tuplas, [(100, 0, barco), (60, 2, barco), (40, 1, barco), (10, 3, barco)])

class TestDevolverTuplasOrdenadas(unittest.TestCase):
    def testDevolverTuplasOrdenadas(self):
        dino = Dino()
        barcoA = Barco(100)
        barcoB = Barco(150)
        barcoC = Barco(200)
        barcoA.setPosicion(0, 0)
        barcoB.setPosicion(0, 1)
        barcoC.setPosicion(0, 2)
        matriz = [[10, 60, 30], [100, 3, 40], [50, 70, 80]]
        partida = Partida(matriz, [barcoA, barcoB, barcoC], 1, dino)
        tuplas = dino.devolverTuplasOrdenadasDanioTurnoBarco(partida)
        self.assertEqual(tuplas, [(100, 0, barcoB), (80, 2, barcoC), (70, 1, barcoC), (60, 1, barcoA), (50, 0, barcoC), (40, 2, barcoB), (30, 2, barcoA), (10, 0, barcoA), (3, 1, barcoB)])

if __name__ == '__main__':
	unittest.main()