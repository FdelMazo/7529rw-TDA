import unittest

from GrafoPesado import *

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