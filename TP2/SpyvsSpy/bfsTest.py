import unittest
import random

from grafo import *
from bfs import *

def crearGrafo():
    vertices = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]
    grafo = Grafo()
    for v in vertices:
        grafo.agregarVertice(v)
    grafo.agregarArista((1, 2), (3, 4))
    grafo.agregarArista((1, 2), (5, 6))
    grafo.agregarArista((5, 6), (7, 8))
    grafo.agregarArista((5, 6), (9, 10))
    grafo.agregarArista((7, 8), (11, 12))
    grafo.agregarArista((9, 10), (11, 12))
    grafo.agregarArista((11, 12), (17, 18))
    grafo.agregarArista((17, 18), (15, 16))
    grafo.agregarArista((9, 10), (13, 14))
    grafo.agregarArista((13, 14), (15, 16))
    return grafo


class testminimoCaminoSinPesosOrigenYFinalIguales(unittest.TestCase):
    def test01(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (1, 2)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertEqual([(1, 2)], camino)

class testNivel0HayUnUnicoVerticeYEsElCorrecto(unittest.TestCase):
    def test02(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (15, 16)
        orden, nivel = bfs(grafo, origen, final)
        self.assertEqual(nivel[0], (1, 2))

class testNivel1HayDosUnicosVerticesYSonLosCorrectos(unittest.TestCase):
    def test03(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (15, 16)
        orden, nivel = bfs(grafo, origen, final)
        self.assertTrue(len(nivel[1]) == 2 and ((3, 4) in nivel[1]) and ((5, 6) in nivel[1]))

class testUnicoCaminoMinimoCorrecto1(unittest.TestCase):
    def test04(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (15, 16)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertEqual([(1, 2), (5, 6), (9, 10), (13, 14), (15, 16)], camino)

class testUnicoCaminoMinimoCorrecto2(unittest.TestCase):
    def test05(self):
        grafo = crearGrafo()
        origen = (9, 10)
        final = (15, 16)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertEqual([(9, 10), (13, 14), (15, 16)], camino)

class testObtenerUnoDeLosDosCaminosPosibles(unittest.TestCase):
    def test06(self):
        grafo = crearGrafo()
        origen = (5, 6)
        final = (17, 18)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertEqual([(5, 6), (9, 10), (11, 12), (17, 18)] or [(5, 6), (7, 8), (11, 12), (17, 18)], camino)

if __name__ == '__main__':
	unittest.main()