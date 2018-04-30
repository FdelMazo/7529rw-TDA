import unittest
import random

from GrafoPesado import *
from Dijkstra import *

def crearGrafo1():
    grafo = GrafoPesado()
    vertices = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]
    aristas = [
        ( (1, 2), (3, 4) ),
        ( (1, 2), (5, 6) ),
        ( (5, 6), (7, 8) ),
        ( (5, 6), (9, 10) ),
        ( (7, 8), (11, 12) ),
        ( (9, 10), (11, 12) ),
        ( (11, 12), (17, 18) ),
        ( (17, 18), (15, 16) ),
        ( (9, 10), (13, 14) ),
        ( (13, 14), (15, 16) )
    ]
    for v in vertices:
        grafo.add(v)
    for v1,v2 in aristas:
        grafo.agregarArista(v1,v2)
    return grafo

def crearGrafo2():
    grafo = GrafoPesado()
    vertices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (10, 10), (20, 20), (30, 30), (40, 40), (50, 50)]
    aristas = [
        ( (1, 1), (2, 2) ),
        ( (1, 1), (3, 3) ),
        ( (1, 1), (4, 4) ),
        ( (1, 1), (5, 5) ),
        ( (2, 2), (10, 10) ),
        ( (3, 3), (10, 10) ),
        ( (2, 2), (5, 5) ),
        ( (5, 5), (6, 6) ),
        ( (10, 10), (6, 6) ),
        ( (6, 6), (7, 7) ),
        ( (6, 6), (20, 20) ),
        ( (4, 4), (40, 40) ),
        ( (50, 50), (20, 20) ),
        ( (50, 50), (40, 40) ),
        ( (20, 20), (40, 40) ),
        ( (10, 10), (20, 20) )
    ]
    for v in vertices:
        grafo.add(v)
    for v1,v2 in aristas:
        grafo.agregarArista(v1,v2)
    return grafo

class testMinimoCaminoConPeso(unittest.TestCase):
    def test01MinimoCaminoConPesosOrigenYFinalIguales(self):
        grafo = GrafoPesado()
        origen = (1, 2)
        final = (1, 2)
        grafo.agregarArista((1,2),(1,2))
        camino,d = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 2)], camino)

    def test02MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo1()
        origen = (1, 2)
        final = (11, 12)
        camino,d = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 2), (5, 6), (7, 8), (11, 12)], camino)

    def test03MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo1()
        origen = (1, 2)
        final = (15, 16)
        camino,d = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 2), (5, 6), (9, 10), (13, 14), (15, 16)], camino)

    def test04MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo2()
        origen = (1, 1)
        final = (6, 6)
        camino,d = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 1), (2, 2), (5, 5), (6, 6)], camino)

    def test05MinimoCaminoConPesosCorrecto(self):
        grafo = crearGrafo2()
        origen = (1, 1)
        final = (40, 40)
        camino,d = minimoCaminoConPeso(grafo, origen, final)
        self.assertEqual([(1, 1), (4, 4), (40, 40)], camino)

    def test06MinimoCaminoConPesosCorrecto(self):
        grafo1 = crearGrafo2()
        origen = (1, 1)
        final = (20, 20)
        camino,d = minimoCaminoConPeso(grafo1, origen, final)
        self.assertEqual([(1, 1), (2, 2), (5, 5), (6, 6), (20, 20)], camino)
    
if __name__ == '__main__':
	unittest.main()