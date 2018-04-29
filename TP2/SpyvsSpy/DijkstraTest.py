import unittest
import random

from grafo import *
from Dijkstra import *

def crearGrafo1():
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

def crearGrafo2():
    vertices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (10, 10), (20, 20), (30, 30), (40, 40), (50, 50)]
    grafo = Grafo()
    for v in vertices:
        grafo.agregarVertice(v)
    grafo.agregarArista((1, 1), (2, 2))
    grafo.agregarArista((1, 1), (3, 3))
    grafo.agregarArista((1, 1), (4, 4))
    grafo.agregarArista((1, 1), (5, 5))
    grafo.agregarArista((2, 2), (10, 10))
    grafo.agregarArista((3, 3), (10, 10))
    grafo.agregarArista((2, 2), (5, 5))
    grafo.agregarArista((5, 5), (6, 6))
    grafo.agregarArista((10, 10), (6, 6))
    grafo.agregarArista((6, 6), (7, 7))
    grafo.agregarArista((6, 6), (20, 20))
    grafo.agregarArista((4, 4), (40, 40))
    grafo.agregarArista((50, 50), (7, 7))
    grafo.agregarArista((50, 50), (20, 20))
    grafo.agregarArista((50, 50), (40, 40))
    grafo.agregarArista((20, 20), (40, 40))
    grafo.agregarArista((10, 10), (20, 20))
    return grafo


class testMinimoCaminoConPeso(unittest.TestCase):
    def test01MinimoCaminoConPesosOrigenYFinalIguales(self):
        grafo = crearGrafo1()
        origen = (1, 2)
        final = (1, 2)
        camino = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 2)], camino)

    def test02MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo1()
        origen = (1, 2)
        final = (11, 12)
        camino = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 2), (5, 6), (7, 8), (11, 12)], camino)

    def test03MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo1()
        origen = (1, 2)
        final = (15, 16)
        camino = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 2), (5, 6), (9, 10), (13, 14), (15, 16)], camino)

    def test04MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo2()
        origen = (1, 1)
        final = (6, 6)
        camino = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 1), (2, 2), (5, 5), (6, 6)], camino)

    def test05MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo2()
        origen = (1, 1)
        final = (40, 40)
        camino = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 1), (4, 4), (40, 40)], camino)

    def test06MinimoCaminoConPesosCorrecto(self):
        grafo1 = crearGrafo2()
        origen = (1, 1)
        final = (20, 20)
        camino = minimoCaminoConPeso(grafo1, origen, final)
        self.assertEqual([(1, 1), (2, 2), (5, 5), (6, 6), (20, 20)], camino)
    
if __name__ == '__main__':
	unittest.main()