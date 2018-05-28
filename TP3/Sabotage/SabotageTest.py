import unittest
from Sabotage import *

class SabotageTest(unittest.TestCase):

	def test_carga_del_archivo_exitosa(self):
		red = RedDeTransporte()
		red.agregarVertice(2)
		red.agregarArista(0, 2, 10)
		red.agregarArista(2, 1, 5)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa1.map")
		self.assertTrue(red.esIgualA(red2))
	

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(SabotageTest)
	unittest.TextTestRunner(verbosity=1).run(suite)
