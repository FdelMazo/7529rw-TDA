import unittest
from RedDeTransporte import *
from FlujoMaximo import *

class FlujoMaximoTest(unittest.TestCase):

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


	def test_red_tiene_el_flujo_maximo_esperado17(self):
		red = RedDeTransporte()
		red.agregarArista(0,2,10)
		red.agregarArista(2,1,5)
		red.agregarArista(2,3,1)
		red.agregarArista(2,4,2)
		red.agregarArista(0,3,3)
		red.agregarArista(3,4,6)
		red.agregarArista(4,1,5)
		red.agregarArista(0,5,1)
		red.agregarArista(5,3,3)
		red.agregarArista(5,4,3)
		red.agregarArista(5,1,10)	
		self.assertEquals( 11, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado18(self):
		''' Ford-Fulkerson in 5 minutes — Step by step example'''
		red = RedDeTransporte()
		red.agregarArista(0,2,10)
		red.agregarArista(2,3,4)
		red.agregarArista(2,4,2)
		red.agregarArista(2,5,8)	
		red.agregarArista(3,1,10)
		red.agregarArista(0,4,10)
		red.agregarArista(4,5,9)
		red.agregarArista(5,3,6)
		red.agregarArista(5,1,10)
		self.assertEquals( 19, flujoMaximo(red) )


	def test_red_tiene_el_flujo_maximo_esperado19(self):
		'''
		https://brilliant.org/wiki/ford-fulkerson-algorithm/
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,4)
		red.agregarArista(2,3,4)
		red.agregarArista(3,1,2)
		red.agregarArista(0,4,3)
		red.agregarArista(4,5,6)
		red.agregarArista(5,1,6)
		red.agregarArista(3,4,3)
		self.assertEquals( 7, flujoMaximo(red) )

	def test_red_tiene_el_flujo_maximo_esperado20(self):
		'''
		Ford Fulkerson algorithm for Max Flow
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,9)
		red.agregarArista(2,3,8)
		red.agregarArista(3,1,10)
		red.agregarArista(0,4,9)
		red.agregarArista(4,5,3)
		red.agregarArista(5,1,7)
		red.agregarArista(4,3,1)
		red.agregarArista(2,4,10)
		red.agregarArista(5,3,8)
		self.assertEquals( 12, flujoMaximo(red) )
	
	def test_red_tiene_el_flujo_maximo_esperado21(self):
		'''
		Graph : Maximum Flow Ford-Fulkerson Algorithm
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,10)
		red.agregarArista(2,3,9)
		red.agregarArista(2,4,4)
		red.agregarArista(2,5,15)
		red.agregarArista(3,1,10)
		red.agregarArista(3,5,15)
		red.agregarArista(0,4,5)
		red.agregarArista(4,5,8)
		red.agregarArista(5,1,10)
		red.agregarArista(5,7,15)
		red.agregarArista(4,6,4)
		red.agregarArista(0,6,15)
		red.agregarArista(7,4,6)
		red.agregarArista(6,7,16)
		red.agregarArista(7,1,10)
		self.assertEquals( 28, flujoMaximo(red))
	
	
	def test_red_tiene_el_flujo_maximo_esperado22(self):
		'''
		https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,16)
		red.agregarArista(2,3,12)
		red.agregarArista(3,1,20)
		red.agregarArista(2,4,10)
		red.agregarArista(3,4,9)
		red.agregarArista(4,2,4)
		red.agregarArista(0,4,13)
		red.agregarArista(4,5,14)
		red.agregarArista(5,1,4)
		red.agregarArista(5,3,7)
		self.assertEquals( 23, flujoMaximo(red))
	


	def test_red_tiene_el_flujo_maximo_esperado23(self):
		'''
		https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,1000)
		red.agregarArista(2,1,1000)
		red.agregarArista(2,3,1)
		red.agregarArista(0,3,1000)
		red.agregarArista(3,1,1000)
		self.assertEquals( 2000, flujoMaximo(red))
	
	
	def test_red_tiene_el_flujo_maximo_esperado24(self):
		'''
		http://www.cs.ucc.ie/~gprovan/CS4407/Ford-Fulkerson-lecture1.pdf
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,16)
		red.agregarArista(2,3,12)
		red.agregarArista(3,1,20)
		red.agregarArista(0,4,13)
		red.agregarArista(4,2,4)
		red.agregarArista(2,4,10)
		red.agregarArista(4,5,14)
		red.agregarArista(5,1,4)
		red.agregarArista(5,3,7)
		red.agregarArista(3,4,9)
		self.assertEquals( 23, flujoMaximo(red))
	
	
	def test_red_tiene_el_flujo_maximo_esperado25(self):
		'''
		http://www.cs.ucc.ie/~gprovan/CS4407/Ford-Fulkerson-lecture1.pdf 
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,2)
		red.agregarArista(2,1,4)
		red.agregarArista(0,3,5)
		red.agregarArista(2,3,1)
		red.agregarArista(3,1,3)
		self.assertEquals( 5, flujoMaximo(red))
	
	
	def test_red_tiene_el_flujo_maximo_esperado26(self):
		'''
		https://www.teiresias.muni.cz/amalg/www/adaptation/fold-fulkerson
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,1)
		red.agregarArista(2,3,1)
		red.agregarArista(3,1,3)
		red.agregarArista(2,4,1)
		red.agregarArista(4,3,2)
		red.agregarArista(0,4,5)
		red.agregarArista(4,1,1)
		red.agregarArista(4,5,1)
		red.agregarArista(4,6,2)
		red.agregarArista(0,5,1)
		red.agregarArista(5,6,1)
		red.agregarArista(6,1,3)
		self.assertEquals( 7, flujoMaximo(red))


	def test_red_tiene_el_flujo_maximo_esperado27(self):
		'''
		http://sisdin.unipv.it/labsisdin/teaching/courses/ails/files/Ford-Fulkerson_example.pdf
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,9)
		red.agregarArista(2,4,9)
		red.agregarArista(2,5,4)
		red.agregarArista(2,6,3)
		red.agregarArista(4,1,7)
		red.agregarArista(4,5,2)
		red.agregarArista(0,3,12)
		red.agregarArista(2,3,6)
		red.agregarArista(3,6,3)
		red.agregarArista(3,4,2)
		red.agregarArista(3,5,6)
		red.agregarArista(5,1,8)
		red.agregarArista(5,6,2)
		red.agregarArista(6,1,5)
		self.assertEquals( 20, flujoMaximo(red))
	


	def test_red_tiene_el_flujo_maximo_esperado28(self):
		'''
		https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=3&cad
		=rja&uact=8&ved=0ahUKEwiagr69gajbAhVKhpAKHYvSAHYQtwIIMzAC&url=https%3A%2
		F%2Fwww.youtube.com%2Fwatch%3Fv%3DrLIR89YyNjg&usg=AOvVaw0czhvPEsCuSSBL2qJ
		2wEV3
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,16)
		red.agregarArista(2,3,12)
		red.agregarArista(3,1,5)
		red.agregarArista(2,4,4)
		red.agregarArista(3,4,9)
		red.agregarArista(3,5,7)
		red.agregarArista(0,4,5)
		red.agregarArista(4,5,20)
		red.agregarArista(5,1,20)
		self.assertEquals( 21, flujoMaximo(red))


	def test_red_tiene_el_flujo_maximo_esperado29(self):
		'''
		https://www.youtube.com/watch?v=9FICcDgreOE
		'''
		
		red = RedDeTransporte()
		red.agregarArista(0,2,16)
		red.agregarArista(2,3,12)
		red.agregarArista(3,1,20)
		red.agregarArista(0,4,13)
		red.agregarArista(4,2,4)
		red.agregarArista(3,4,9)
		red.agregarArista(4,5,14)
		red.agregarArista(5,3,7)
		red.agregarArista(5,1,4)
		self.assertEquals( 23, flujoMaximo(red))


	def test_red_tiene_el_flujo_maximo_esperado30(self):
		'''
		https://www.youtube.com/watch?v=3LG-My_MoWc
		'''
		
		red = RedDeTransporte()
		red.agregarArista(0,2,10)
		red.agregarArista(2,3,4)
		red.agregarArista(3,1,10)
		red.agregarArista(0,4,10)
		red.agregarArista(2,4,2)
		red.agregarArista(4,5,9)
		red.agregarArista(5,1,10)
		red.agregarArista(5,3,6)
		red.agregarArista(2,5,8)
		self.assertEquals( 19, flujoMaximo(red))


	def test_red_tiene_el_flujo_maximo_esperado31(self):
		'''
		https://www.youtube.com/watch?v=GiN3jRdgxU4
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,2)
		red.agregarArista(2,1,3)
		red.agregarArista(0,4,3)
		red.agregarArista(4,2,1)
		red.agregarArista(4,5,1)
		red.agregarArista(5,1,3)
		self.assertEquals( 4, flujoMaximo(red))


	def test_red_tiene_el_flujo_maximo_esperado32(self):
		'''
		https://www.youtube.com/watch?v=7jFoyLk2VjM
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,5)
		red.agregarArista(2,3,6)
		red.agregarArista(3,1,6)
		red.agregarArista(0,4,5)
		red.agregarArista(4,3,3)
		red.agregarArista(4,5,1)
		red.agregarArista(2,5,3)	
		red.agregarArista(5,1,6)
		self.assertEquals( 9, flujoMaximo(red))


	def test_red_tiene_el_flujo_maximo_esperado33(self):
		'''
		Ford Fulkerson max flow
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,10)
		red.agregarArista(2,3,9)
		red.agregarArista(3,1,10)
		red.agregarArista(0,4,5)
		red.agregarArista(4,5,8)
		red.agregarArista(5,1,10)
		red.agregarArista(2,4,4)
		red.agregarArista(5,2,15)
		red.agregarArista(3,5,15)
		red.agregarArista(0,6,15)
		red.agregarArista(4,6,4)
		red.agregarArista(6,7,16)
		red.agregarArista(7,4,6)
		red.agregarArista(7,5,4)
		red.agregarArista(7,1,10)
		self.assertEquals( 29, flujoMaximo(red))


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(FlujoMaximoTest)
	unittest.TextTestRunner(verbosity=1).run(suite)
