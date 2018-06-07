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
		self.assertEquals(str(red), (
		"(0,2) [1]\n" +
		"(2,1) [1]\n" ) )


	def test_agregar_vertice_y_arista_en_red_de_transporte2(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2)
		red.agregarArista(2, 3)
		red.agregarArista(2, 4)
		red.agregarArista(3, 1)
		red.agregarArista(0, 4)
		red.agregarArista(4, 3)
		red.agregarArista(4, 5)
		red.agregarArista(5, 3)
		red.agregarArista(5, 1)
		self.assertEquals(str(red), (
		"(0,2) [1]\n" +
		"(0,4) [1]\n" +
		"(2,3) [1]\n" +
		"(2,4) [1]\n" +
		"(3,1) [1]\n" +
		"(4,3) [1]\n" +
		"(4,5) [1]\n" +
		"(5,3) [1]\n" +
		"(5,1) [1]\n" ) )


	def test_fuente_tiene_los_adyacentes_esperados(self):
		red = RedDeTransporte()
		adyacentesEsperados = []
		adyacentesEsperados.append(red.obtenerSumidero())
		red.agregarArista(0,1)
		self.assertEquals(red.obtenerFuente().obtenerAdyacentes(), 
		adyacentesEsperados)
	
	
	def test_fuente_tiene_los_adyacentes_esperados2(self):
		red = RedDeTransporte()
		adyacentesEsperados = []
		red.agregarArista(0,1)
		adyacentesEsperados.append(red.obtenerSumidero())
		red.agregarArista(0,2)
		adyacentesEsperados.append(red.obtenerVertice(2))
		red.agregarArista(2,1)
		self.assertEquals(red.obtenerFuente().obtenerAdyacentes(), 
		adyacentesEsperados)


	def test_fuente_tiene_los_adyacentes_esperados3(self):
		red = RedDeTransporte()
		adyacentesEsperados = []
		red.agregarArista(0, 2, 1)
		adyacentesEsperados.append(red.obtenerVertice(2))
		red.agregarArista(2, 1, 1)
		red.agregarArista(0, 1, 10)
		adyacentesEsperados.append(red.obtenerSumidero())
		self.assertEquals(red.obtenerFuente().obtenerAdyacentes(), 
		adyacentesEsperados)


	def test_fuente_tiene_aristas_esperadas(self):
		red = RedDeTransporte()
		aristasEsperadas = []
		red.agregarArista(0,1)
		aristasEsperadas += red.obtenerAristasDesdeHasta(0,1)
		self.assertEquals(red.obtenerAristas(red.obtenerFuente().obtenerNumero()), 
		aristasEsperadas)


	def test_fuente_tiene_aristas_esperadas2(self):
		red = RedDeTransporte()
		aristasEsperadas = []
		red.agregarArista(0,1, 10)
		aristasEsperadas += red.obtenerAristasDesdeHasta(0,1)
		red.agregarArista(2,1, 11)
		self.assertEquals(red.obtenerAristas(red.obtenerFuente().obtenerNumero()), 
		aristasEsperadas)


	def test_fuente_tiene_aristas_esperadas3(self):
		red = RedDeTransporte()
		aristasEsperadas = []
		red.agregarArista(0,1, 10)
		aristasEsperadas += red.obtenerAristasDesdeHasta(0,1)
		red.agregarArista(2,1, 11)
		red.agregarArista(0,2, 12)
		aristasEsperadas += red.obtenerAristasDesdeHasta(0,2)
		self.assertEquals(red.obtenerAristas(red.obtenerFuente().obtenerNumero()), 
		aristasEsperadas)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(RedDeTransporteTest)
	unittest.TextTestRunner(verbosity=1).run(suite)
