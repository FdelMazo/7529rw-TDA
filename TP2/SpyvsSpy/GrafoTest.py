import unittest

from Grafo import *
class testGrafoBasico(unittest.TestCase):
    def testVerticePerteneceEnGrafo(self):
        grafo = Grafo()
        vertice1 = (1,1)
        vertice2 = (2,2)
        grafo.add(vertice1)
        grafo.add(vertice2)
        self.assertTrue(vertice1 in grafo and vertice2 in grafo)
        
    def testVerticesAdyacentes(self):
        grafo = Grafo()
        v1,v2 = (1,1), (2,2)
        grafo.agregarArista(v1,v2)
        self.assertTrue(grafo.adyacentes(v1) == [v2])
        self.assertTrue(grafo.adyacentes(v2) == [v1])
    
    def testMultiplesAdyacentes(self):
        grafo = Grafo()
        v1,v2,v3 = (1,1), (2,2), (3,3)
        grafo.agregarArista(v1,v2)
        grafo.agregarArista(v2,v3)
        self.assertTrue(grafo.adyacentes(v1) == [v2])
        self.assertTrue(grafo.adyacentes(v2) == [v1,v3])

class testGrafoPesadoBasico(unittest.TestCase):      
    def testPesoEntreDosVertices(self):
        grafo = GrafoPesado()
        v1,v2 = (1,1), (2,2)
        grafo.agregarArista(v1,v2)
        self.assertTrue(grafo.distancia(v1,v2) == math.sqrt(2))
        grafo = GrafoPesado()
        v3,v4 = (3,3), (3,5)
        grafo.agregarArista(v3,v4)
        self.assertTrue(grafo.distancia(v3,v4) == 2)
    
if __name__ == '__main__':
	unittest.main()