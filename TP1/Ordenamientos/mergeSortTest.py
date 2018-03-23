import unittest
from mergeSort import mergeSort
from generarArrayRandom import generarArrayRandom

class TestSelectionSort(unittest.TestCase):

	def test01OrdenarListaVacia(self):
		array = []
		result = []
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

	def test02OrdenarListaDe2Elementos(self):
		array = [2, 1]
		result = [1, 2]
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

	def test03OrdenarListaDe500Elementos(self):
		array = generarArrayRandom(500, 0, 1000)
		result = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)

	def test04OrdenarListaDe500ElementosNegativos(self):
		array = generarArrayRandom(500, -1000, 0)
		result = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(result, arrayOrdenado)


if __name__ == '__main__':
	unittest.main()
