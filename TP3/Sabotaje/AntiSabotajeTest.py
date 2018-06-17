import unittest
from RedDeTransporte import *
from AntiSabotaje import *

def lasAristasProtegidasSonCorrectas(aristasAProteger, aristasProtegidas):
	aristasOk = True
	
	for a in aristasProtegidas:
		mismasAristas = False
			
		for a2 in aristasAProteger:
			if a.esIgualA(a2):
				mismasAristas = True
			
		if not mismasAristas:
			aristasOk = False
			break
				
	return aristasOk


class SabotajeTest(unittest.TestCase):

	def test_proteger_dos_aritas_protege_las_aristas_esperadas(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa1.map")
		aristasAProteger = [ 
		red.obtenerAristasDesdeHasta(0,2)[0], 
		red.obtenerAristasDesdeHasta(2,1)[0]
		]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))
		
	
	def test_proteger_dos_aritas_protege_las_aristas_esperadas2(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa5.map")
		aristasAProteger = [ 
		red.obtenerAristasDesdeHasta(0,1)
		][0]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))
	
	
	def test_proteger_dos_aritas_protege_las_aristas_esperadas3(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa4.map")
		aristasAProteger =  red.obtenerAristasDesdeHasta(0,1)
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas4(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa8.map")
		aristasAProteger =  red.obtenerAristasDesdeHasta(0,1)
		aristasAProteger.pop()
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas5(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa9.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,1)[0],
		red.obtenerAristasDesdeHasta(0,1)[1] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))

	
	def test_proteger_dos_aritas_protege_las_aristas_esperadas6(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa38.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(3,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))
	

	def test_proteger_dos_aritas_protege_las_aristas_esperadas7(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa7.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(0,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas8(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa39.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(0,4)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas9(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa3.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(2,3)[0],
		red.obtenerAristasDesdeHasta(4,5)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))

	
	def test_proteger_dos_aritas_protege_las_aristas_esperadas10(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa6.map")
		aristasAProteger =  red.obtenerAristasDesdeHasta(0,1)
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas11(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa12.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,1)[0],
		red.obtenerAristasDesdeHasta(0,2)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas12(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa14.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(2,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas)) 


	def test_proteger_dos_aritas_protege_las_aristas_esperadas13(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa40.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(3,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas14(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa41.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(0,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))
	
	
	def test_proteger_dos_aritas_protege_las_aristas_esperadas15(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa10.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,1)[1],
		red.obtenerAristasDesdeHasta(0,1)[2] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas16(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa11.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(2,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas17(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa11.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(2,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas18(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa13.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(2,3)[0],
		red.obtenerAristasDesdeHasta(0,2)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas19(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa15.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(0,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas20(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa16.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(0,4)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas21(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa18.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(3,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas22(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa19.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(2,1)[0],
		red.obtenerAristasDesdeHasta(4,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas23(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa20.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(2,1)[0],
		red.obtenerAristasDesdeHasta(4,1)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas24(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa21.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(2,1)[0],
		red.obtenerAristasDesdeHasta(0,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas25(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa22.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(4,5)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas26(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa23.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,4)[0],
		red.obtenerAristasDesdeHasta(0,2)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas27(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa24.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(2,3)[0],
		red.obtenerAristasDesdeHasta(0,2)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas28(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa25.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(2,3)[0],
		red.obtenerAristasDesdeHasta(0,2)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas29(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa42.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(5,6)[0],
		red.obtenerAristasDesdeHasta(4,5)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas30(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa43.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(4,1)[0],
		red.obtenerAristasDesdeHasta(0,2)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas31(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa44.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(0,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas32(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa27.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(0,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas33(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa30.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(4,6)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))


	def test_proteger_dos_aritas_protege_las_aristas_esperadas34(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa37.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(2,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))
	
	
	def test_proteger_dos_aritas_protege_las_aristas_esperadas35(self):
		red = cargarArchivoAntiSabotaje("MapasDePrueba/mapa45.map")
		aristasAProteger =  [ red.obtenerAristasDesdeHasta(0,2)[0],
		red.obtenerAristasDesdeHasta(2,3)[0] ]
		aristasProtegidas = proteger2Aristas(red)
		self.assertTrue(lasAristasProtegidasSonCorrectas(
		aristasAProteger,
		aristasProtegidas))
	

	def test_carga_del_archivo_exitosa(self):
		red = RedDeTransporte()
		red.agregarVertice(2)
		red.agregarArista(0, 2, 10)
		red.agregarArista(2, 1, 5)
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa1.map")
		self.assertTrue(red.esIgualA(red2))
	

	def test_carga_del_archivo_exitosa2(self):
		red = RedDeTransporte()
		red.agregarArista(0, 2, 9)
		red.agregarArista(2, 3, 8)
		red.agregarArista(2, 4, 10)
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa2.map")
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
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa3.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa4(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa4.map")
		self.assertTrue(red.esIgualA(red2))
	
	
	def test_carga_del_archivo_exitosa5(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa5.map")
		self.assertTrue(red.esIgualA(red2))
	

	def test_carga_del_archivo_exitosa6(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa6.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa7(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa8.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa8(self):
		red = RedDeTransporte()
		red.agregarArista(0, 1, 1)
		red.agregarArista(0, 1, 2)
		red.agregarArista(0, 1, 1)
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa9.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa9(self):
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
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa36.map")
		self.assertTrue(red.esIgualA(red2))


	def test_carga_del_archivo_exitosa10(self):
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
		red2 = cargarArchivoAntiSabotaje("MapasDePrueba/mapa37.map")
		self.assertTrue(red.esIgualA(red2))


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(SabotajeTest)
	unittest.TextTestRunner(verbosity=1).run(suite)
