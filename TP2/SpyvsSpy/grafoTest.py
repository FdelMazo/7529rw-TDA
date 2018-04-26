import unittest

from grafo import *

class testSonAdyacentes(unittest.TestCase):
    def testSonAdyacentes(self):
        grafo = Grafo()
        vertice1 = (4, 5)
        vertice2 = (1, 1)
        grafo.agregarVertice(vertice1)
        grafo.agregarVertice(vertice2)
        grafo.agregarArista(vertice1, vertice2)
        adyacentes1 = grafo.getAdyacentes(vertice1)
        self.assertTrue(vertice2 in adyacentes1.keys())

class testLaDistanciaEs2(unittest.TestCase):
    def testLaDistanciaEs2(self):
        grafo = Grafo()
        vertice1 = (5, 3)
        vertice2 = (3, 3)
        resultado = grafo.calcularDistancia(vertice1, vertice2)
        self.assertEqual(resultado, 2)