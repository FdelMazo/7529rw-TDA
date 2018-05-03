import unittest
from KMP_matching import *

class PruebaKRP(unittest.TestCase):
	
	def test_dos_cadenas_iguales_hacen_match(self):
		self.assertTrue(KMP_matching("hola","hola"))
	
	def test_dos_cadenas_iguales_hacen_match2(self):
		self.assertTrue(KMP_matching("silla","silla"))
	
	def test_substring_tiene_el_match_esperado(self):
		self.assertTrue(KMP_matching("hola","h"))
	
	def test_substring_tiene_el_match_esperado2(self):
		self.assertTrue(KMP_matching("hola","o"))

	def test_substring_tiene_el_match_esperado3(self):
		self.assertTrue(KMP_matching("hola","l"))
	
	def test_substring_tiene_el_match_esperado4(self):
		self.assertTrue(KMP_matching("hola","a"))

	def test_substring_tiene_el_match_esperado5(self):
		self.assertTrue(KMP_matching("hola","ho"))
	
	def test_substring_tiene_el_match_esperado6(self):
		self.assertTrue(KMP_matching("hola","ol"))

	def test_substring_tiene_el_match_esperado7(self):
		self.assertTrue(KMP_matching("hola","la"))
	
	def test_substring_tiene_el_match_esperado8(self):
		self.assertTrue(KMP_matching("silla","s"))
	
	def test_substring_tiene_el_match_esperado9(self):
		self.assertTrue(KMP_matching("silla","i"))

	def test_substring_tiene_el_match_esperado10(self):
		self.assertTrue(KMP_matching("silla","l"))
	
	def test_substring_tiene_el_match_esperado11(self):
		self.assertTrue(KMP_matching("silla","a"))

	def test_substring_tiene_el_match_esperado12(self):
		self.assertTrue(KMP_matching("silla","si"))
	
	def test_substring_tiene_el_match_esperado13(self):
		self.assertTrue(KMP_matching("silla","ill"))

	def test_substring_tiene_el_match_esperado14(self):
		self.assertTrue(KMP_matching("silla","lla"))
	
	def test_substring_tiene_el_match_esperado15(self):
		self.assertTrue(KMP_matching("hola","hol"))
	
	def test_substring_tiene_el_match_esperado16(self):
		self.assertTrue(KMP_matching("hola","ola"))
	
	def test_substring_tiene_el_match_esperado17(self):
		self.assertTrue(KMP_matching("Así","í"))
	
	def test_substring_tiene_el_match_esperado18(self):
		self.assertTrue(KMP_matching("Así","sí"))
	
	def test_substring_tiene_el_match_esperado19(self):
		self.assertTrue(KMP_matching("Así","Así"))
	
	def test_substring_tiene_el_match_esperado20(self):
		self.assertTrue(KMP_matching("a","a"))
	
	def test_substring_tiene_el_match_esperado21(self):
		self.assertTrue(KMP_matching("Paraguas","agua"))
	
	def test_substring_tiene_el_match_esperado22(self):
		self.assertTrue(KMP_matching("Paraguas","aguas"))
	
	def test_substring_tiene_el_match_esperado23(self):
		self.assertTrue(KMP_matching("Paraguas","Para"))
	
	def test_substring_tiene_el_match_esperado24(self):
		self.assertTrue(KMP_matching("electroencefalografista","electro"))
	
	def test_cadena_no_substring_no_hace_match25(self):
		self.assertTrue(KMP_matching("silla","lla"))
	
	def test_cadena_no_substring_no_hace_match(self):
		self.assertFalse(KMP_matching("hola","ah"))
	
	def test_cadena_no_substring_no_hace_match2(self):
		self.assertFalse(KMP_matching("hola","oa"))

	def test_cadena_no_substring_no_hace_match3(self):
		self.assertFalse(KMP_matching("hola","al"))
	
	def test_substring_tiene_el_match_esperado4(self):
		self.assertFalse(KMP_matching("hola","oll"))
	
	def test_cadena_no_substring_no_hace_match5(self):
		self.assertFalse(KMP_matching("silla","asi"))

	def test_cadena_no_substring_no_hace_match6(self):
		self.assertFalse(KMP_matching("silla","p"))
		
	def test_cadena_no_substring_no_hace_match7(self):
		self.assertFalse(KMP_matching("electroencefalografista","electroencefalografistaa"))
	
	def test_cadena_no_substring_no_hace_match8(self):
		self.assertFalse(KMP_matching("silla","llla"))
	
	def test_cadena_no_substring_no_hace_match9(self):
		self.assertFalse(KMP_matching("electroencefalografista","llectroencefalografista"))
	
	def test_cadena_no_substring_no_hace_match10(self):
		self.assertFalse(KMP_matching("Así","i"))
	
	def test_cadena_no_substring_no_hace_match11(self):
		self.assertFalse(KMP_matching("Así","íAs"))
	
	def test_cadena_no_substring_no_hace_match12(self):
		self.assertFalse(KMP_matching("Paraguas","para"))

	def test_cadena_no_substring_no_hace_match13(self):
		self.assertFalse(KMP_matching("silla","silll"))

	def test_cadena_no_substring_no_hace_match14(self):
		self.assertFalse(KMP_matching("silla","illaa"))

	def test_cadena_no_substring_no_hace_match15(self):
		self.assertFalse(KMP_matching("silla","illas"))

	def test_cadena_no_substring_no_hace_match16(self):
		self.assertFalse(KMP_matching("silla","llas"))

'''Forma de ejecutar según la doc. de python'''  
if __name__ == '__main__':
	unittest.main()
	'''suite = unittest.TestLoader().loadTestsFromTestCase(PruebaKRP)
	unittest.TextTestRunner(verbosity=2).run(suite)'''
	
