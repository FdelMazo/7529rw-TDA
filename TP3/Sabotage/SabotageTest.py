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
	
	
	def test_carga_del_archivo_exitosa2(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 9)
		red.agregarArista(2, 3, 8)
		red.agregarArista(2, 4, 10)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa2.map")
		self.assertTrue(red.esIgualA(red2))
	
	
	def test_carga_del_archivo_exitosa3(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa3.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa4(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa4.map")
		self.assertTrue(red.esIgualA(red2))
	
	
	def test_carga_del_archivo_exitosa5(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa5.map")
		self.assertTrue(red.esIgualA(red2))
	

	def test_carga_del_archivo_exitosa6(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa6.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa7(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa7.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa8(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa8.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa9(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa9.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa10(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa10.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa11(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 1)
		red.agregarArista(2, 1, 1)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa11.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa12(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 1)
		red.agregarArista(2, 1, 1)
		red.agregarArista(0, 1, 10)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa12.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa13(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa13.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa14(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 20)
		red.agregarArista(2, 1, 10)
		red.agregarArista(0, 3, 10)
		red.agregarArista(2, 3, 30)
		red.agregarArista(3, 1, 20)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa14.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa15(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 100)
		red.agregarArista(2, 1, 100)
		red.agregarArista(0, 3, 100)
		red.agregarArista(2, 3, 1)
		red.agregarArista(3, 1, 100)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa15.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa16(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 100)
		red.agregarArista(2, 3, 100)
		red.agregarArista(3, 1, 100)
		red.agregarArista(2, 1, 1)
		red.agregarArista(4, 1, 1)
		red.agregarArista(0, 4, 100)
		red.agregarArista(4, 5, 100)
		red.agregarArista(5, 1, 100)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa16.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa17(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2)
		red.agregarArista(2, 1)
		red.agregarArista(0, 3)
		red.agregarArista(3, 1)
		red.agregarArista(2, 3)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa17.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa18(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 2)
		red.agregarArista(2, 1, 4)
		red.agregarArista(0, 3, 4)
		red.agregarArista(3, 1, 2)
		red.agregarArista(2, 3, 6)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa18.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa19(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa19.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa20(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa20.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa21(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa21.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa22(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa22.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa23(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa23.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa24(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa24.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa25(self):
		'''
		Ford Fulkerson algorithm for Max Flow
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa25.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa26(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa26.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa27(self):
		'''
		https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,1000)
		red.agregarArista(2,1,1000)
		red.agregarArista(2,3,1)
		red.agregarArista(0,3,1000)
		red.agregarArista(3,1,1000)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa27.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa28(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa28.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa29(self):
		'''
		http://www.cs.ucc.ie/~gprovan/CS4407/Ford-Fulkerson-lecture1.pdf 
		'''
		red = RedDeTransporte()
		red.agregarArista(0,2,2)
		red.agregarArista(2,1,4)
		red.agregarArista(0,3,5)
		red.agregarArista(2,3,1)
		red.agregarArista(3,1,3)
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa29.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa30(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa30.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa31(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa31.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa32(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa32.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa33(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa33.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa34(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa34.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa35(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa35.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa36(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa36.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa37(self):
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
		red2 = cargarArchivoSabotage("MapasDePrueba/mapa37.map")
		self.assertTrue(red.esIgualA(red2))


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(SabotageTest)
	unittest.TextTestRunner(verbosity=1).run(suite)
