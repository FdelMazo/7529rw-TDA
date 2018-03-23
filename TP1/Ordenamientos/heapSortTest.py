import unittest
from heapSort import heapSort
from generarArrayRandom import generarArrayRandom

class TestSelectionSort(unittest.TestCase):

	def test01OrdenarListaVacia(self):
		array = []
		result = []
		heapSort(array)
		self.assertEqual(result, array)

	def test02OrdenarListaDe2Elementos(self):
		array = [2, 1]
		result = [1, 2]
		heapSort(array)
		self.assertEqual(result, array)

	def test03OrdenarListaDe500Elementos(self):
		array = generarArrayRandom(500, 0, 1000)
		result = sorted(array)
		heapSort(array)
		self.assertEqual(result, array)

	def test04OrdenarListaDe1000Elementos(self):
		array = generarArrayRandom(1000, 0, 10000)
		result = sorted(array)
		heapSort(array)
		self.assertEqual(result, array)

if __name__ == '__main__':
	unittest.main()
