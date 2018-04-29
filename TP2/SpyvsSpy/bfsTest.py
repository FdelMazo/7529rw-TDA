import unittest
import random

from Grafo import *
from bfs import *

def crearGrafo():
    grafo = Grafo()
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

class testminimoCaminoSinPesos(unittest.TestCase):
    def test01MinimoCaminoConPesosOrigenYFinalIguales(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (1, 2)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertEqual([(1, 2)], camino)

    def testNivel0HayUnUnicoVerticeYEsElCorrecto(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (15, 16)
        orden, nivel = bfs(grafo, origen, final)
        self.assertEqual(nivel[0], (1, 2))

    def testNivel1HayDosUnicosVerticesYSonLosCorrectos(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (15, 16)
        orden, nivel = bfs(grafo, origen, final)
        self.assertTrue(len(nivel[1]) == 2 and ((3, 4) in nivel[1]) and ((5, 6) in nivel[1]))

    def testUnicoCaminoMinimoCorrecto1(self):
        grafo = crearGrafo()
        origen = (1, 2)
        final = (15, 16)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertEqual([(1, 2), (5, 6), (9, 10), (13, 14), (15, 16)], camino)

    def testUnicoCaminoMinimoCorrecto2(self):
        grafo = crearGrafo()
        origen = (9, 10)
        final = (15, 16)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertEqual([(9, 10), (13, 14), (15, 16)], camino)

    def testObtenerUnoDeLosDosCaminosPosibles(self):
        grafo = crearGrafo()
        origen = (5, 6)
        final = (17, 18)
        camino = minimoCaminoSinPesos(grafo, origen, final)
        self.assertTrue(
            [(5, 6), (9, 10), (11, 12), (17, 18)] == camino
            or [(5, 6), (7, 8), (11, 12), (17, 18)] == camino
        )

if __name__ == '__main__':
	unittest.main()