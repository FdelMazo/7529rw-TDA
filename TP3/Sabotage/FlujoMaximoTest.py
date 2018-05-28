import unittest
from RedDeTransporte import *
from FlujoMaximo import *

class RedDeTransporteTest(unittest.TestCase):

	
	def test_red_tiene_la_arista_minima_esperada(self):
		red = RedDeTransporte()
		red.agregarVertice(2)
		red.agregarArista(0, 2, 10)
		red.agregarArista(2, 1, 5)
		flujo = {}
		inicializarFlujo(red, flujo)
		self.assertEquals( 5, obtenerAristaMinima( red.obtenerAristas() ).obtenerPeso()  )
	
	
	def test_red_tiene_la_arista_minima_esperada2(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 9)
		red.agregarArista(2, 3, 8)
		red.agregarArista(2, 4, 10)
		flujo = {}
		inicializarFlujo(red, flujo)
		self.assertEquals( 8, obtenerAristaMinima( red.obtenerAristas() ).obtenerPeso()  )


	def test_red_tiene_la_arista_minima_esperada3(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 9)
		red.agregarArista(2, 3, 8)
		red.agregarArista(2, 4, 10)
		red.agregarArista(3, 1, 10)
		red.agregarArista(0, 4, 9)
		red.agregarArista(4, 3, 1)
		red.agregarArista(4, 5, 3)
		red.agregarArista(5, 3, 8)
		red.agregarArista(5, 1, 7)
		flujo = {}
		inicializarFlujo(red, flujo)
		self.assertEquals( 1, obtenerAristaMinima( red.obtenerAristas() ).obtenerPeso()  )


	def test_red_tiene_la_arista_minima_esperada4(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		flujo = {}
		inicializarFlujo(red, flujo)
		self.assertEquals( 1, obtenerAristaMinima( red.obtenerAristas() ).obtenerPeso()  )


	def test_red_tiene_el_flujo_maximo_esperado(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		self.assertEquals( 1, flujoMaximo(red) )

	
	def test_red_tiene_el_flujo_maximo_esperado2(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		self.assertEquals( 2, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado3(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		self.assertEquals( 3, flujoMaximo(red) )

	
	def test_red_tiene_el_flujo_maximo_esperado4(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		self.assertEquals( 3, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado5(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		red.agregarArista(0, 1, 1)
		self.assertEquals( 4, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado6(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		self.assertEquals( 4, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado7(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 1)
		red.agregarArista(2, 1, 1)
		self.assertEquals( 1, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado8(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 1)
		red.agregarArista(2, 1, 1)
		red.agregarArista(0, 1, 10)
		self.assertEquals( 11, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado9(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 9)
		red.agregarArista(2, 3, 8)
		red.agregarArista(2, 4, 10)
		red.agregarArista(3, 1, 10)
		red.agregarArista(0, 4, 9)
		red.agregarArista(4, 3, 1)
		red.agregarArista(4, 5, 3)
		red.agregarArista(5, 3, 8)
		red.agregarArista(5, 1, 7)
		flujo = {}
		inicializarFlujo(red, flujo)
		self.assertEquals( 12, flujoMaximo( red) )


	def test_red_tiene_el_flujo_maximo_esperado10(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 20)
		red.agregarArista(2, 1, 10)
		red.agregarArista(0, 3, 10)
		red.agregarArista(2, 3, 30)
		red.agregarArista(3, 1, 20)
		self.assertEquals( 30, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado11(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 100)
		red.agregarArista(2, 1, 100)
		red.agregarArista(0, 3, 100)
		red.agregarArista(2, 3, 1)
		red.agregarArista(3, 1, 100)
		self.assertEquals( 200, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado12(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 100)
		red.agregarArista(2, 3, 100)
		red.agregarArista(3, 1, 100)
		red.agregarArista(2, 1, 1)
		red.agregarArista(4, 1, 1)
		red.agregarArista(0, 4, 100)
		red.agregarArista(4, 5, 100)
		red.agregarArista(5, 1, 100)
		self.assertEquals( 200, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado13(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2)
		red.agregarArista(2, 1)
		red.agregarArista(0, 3)
		red.agregarArista(3, 1)
		red.agregarArista(2, 3)
		self.assertEquals( 2, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado14(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 2)
		red.agregarArista(2, 1, 4)
		red.agregarArista(0, 3, 4)
		red.agregarArista(3, 1, 2)
		red.agregarArista(2, 3, 6)
		self.assertEquals( 4, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado15(self):
		red = RedDeTransporte()
		red.agregarArista(0,2,10)
		red.agregarArista(2,1,5)
		red.agregarArista(2,4,3)
		red.agregarArista(0,3,8)
		red.agregarArista(3,2,3)
		red.agregarArista(3,4,10)
		red.agregarArista(3,5,3)
		red.agregarArista(4,1,8)
		red.agregarArista(0,5,5)
		red.agregarArista(5,4,3)
		red.agregarArista(5,1,5)	
		self.assertEquals( 18, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado16(self):
		red = RedDeTransporte()
		red.agregarArista(0,2,10)
		red.agregarArista(2,1,5)
		red.agregarArista(2,4,3)
		red.agregarArista(0,3,8)
		red.agregarArista(3,2,3)
		red.agregarArista(3,4,10)
		red.agregarArista(3,5,3)
		red.agregarArista(4,1,8)
		red.agregarArista(0,5,5)
		red.agregarArista(5,4,3)
		red.agregarArista(5,1,10)
		self.assertEquals( 21, flujoMaximo(red) )


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(RedDeTransporteTest)
	unittest.TextTestRunner(verbosity=1).run(suite)
