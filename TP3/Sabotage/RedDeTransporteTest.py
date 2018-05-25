import unittest
from RedDeTransporte import *

class RedDeTransporteTest(unittest.TestCase):


	def test_una_nueva_red_de_transporte_no_es_nula(self):
		self.assertTrue(RedDeTransporte() is not None)


	def test_agregar_vertice_con_numero_existe_lanza_value_error(self):
		
		try:
			red = RedDeTransporte()
			red.agregarVertice(1)
			self.assertTrue(False)
			
		except ValueError:
			self.assertTrue(True)
	
	
	def test_agregar_vertice_con_numero_existe_lanza_value_error2(self):
		try:
			red = RedDeTransporte()
			red.agregarVertice(0)
			self.assertTrue(False)
		except ValueError:
			self.assertTrue(True)


	def test_agregar_vertice_y_arista_en_red_de_transporte(self):
		red = RedDeTransporte()
		red.agregarVertice(2)
		red.agregarArista(0, 2)
		red.agregarArista(2, 1)
		self.assertEquals(str(red), '\n0 -> 2 -> 1')


	def test_red_tiene_la_arista_minima_esperada(self):
		red = RedDeTransporte()
		red.agregarVertice(2)
		red.agregarArista(0, 2, 10)
		red.agregarArista(2, 1, 5)
		self.assertEquals( 5, obtenerAristaMinima(obtenerCamino(red)).obtenerPeso() )
		

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(RedDeTransporteTest)
	unittest.TextTestRunner(verbosity=1).run(suite)
