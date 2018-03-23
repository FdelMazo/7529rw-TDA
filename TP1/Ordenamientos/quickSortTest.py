import unittest
from quickSort import quickSort
from generarArrayRandom import generarArrayRandom

class TestQuickSort(unittest.TestCase):

	def test01OrdenarListaVacia(self):
		array = []
		result = []
		quickSort(array)
		self.assertEqual(result, array)

	def test02OrdenarListaDe2Elementos(self):
		array = [2, 1]
		result = [1, 2]
		quickSort(array)
		self.assertEqual(result, array)

	def test03OrdenarListaDe500Elementos(self):
		array = generarArrayRandom(500, 0, 1000)
		result = sorted(array)
		quickSort(array)
		self.assertEqual(result, array)

	def test04OrdenarListaDe500ElementosNegativos(self):
		array = generarArrayRandom(500, -1000, 0)
		result = sorted(array)
		quickSort(array)
		self.assertEqual(result, array)
	
	def test05OrdenarListaOrdenada(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		result = sorted(array)
		quickSort(array)
		self.assertEqual(result, array)


if __name__ == '__main__':
	unittest.main()
