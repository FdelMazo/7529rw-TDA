import unittest
import random

from heapSort import heapSort
from mergeSort import mergeSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from quickSort import quickSort

def generarArrayRandom(n, low, high):
	return [int(n*random.random()) for i in range(low, high)]

class TestListaVacia(unittest.TestCase):

	def test001OrdenarListaVaciaSelectionSort(self):
		array = []
		resultado = []
		selectionSort(array)
		self.assertEqual(resultado, array)

	def test002OrdenarListaVaciaInsertionSort(self):
		array = []
		resultado = []
		insertionSort(array)
		self.assertEqual(resultado, array)

	def test003OrdenarListaVaciaQuickSort(self):
		array = []
		resultado = []
		arrayOrdenado = quickSort(array)
		self.assertEqual(resultado, arrayOrdenado)

	def test004OrdenarListaVaciaheapSort(self):
		array = []
		resultado = []
		heapSort(array)
		self.assertEqual(resultado, array)

	def test005OrdenarListaVaciaMergeSort(self):
		array = []
		resultado = []
		arrayOrdenado = mergeSort(array)
		self.assertEqual(resultado, arrayOrdenado)

class TestListaDe2Elementos(unittest.TestCase):

	def test001OrdenarLista2ElementosSelectionSort(self):
		array = [2, 1]
		resultado = [1, 2]
		selectionSort(array)
		self.assertEqual(resultado, array)

	def test002OrdenarLista2ElementosInsertionSort(self):
		array = [2, 1]
		resultado = [1, 2]
		insertionSort(array)
		self.assertEqual(resultado, array)

	def test003OrdenarLista2ElementosQuickSort(self):
		array = [2, 1]
		resultado = [1, 2]
		arrayOrdenado = quickSort(array)
		self.assertEqual(resultado, arrayOrdenado)

	def test004OrdenarLista2ElementosheapSort(self):
		array = [2, 1]
		resultado = [1, 2]
		heapSort(array)
		self.assertEqual(resultado, array)

	def test005OrdenarLista2ElementosMergeSort(self):
		array = [2, 1]
		resultado = [1, 2]
		arrayOrdenado = mergeSort(array)
		self.assertEqual(resultado, arrayOrdenado)

class TestListaDe500Elementos(unittest.TestCase):

	def test001OrdenarListaDe500ElementosSelectionSort(self):
		array = generarArrayRandom(500, 0, 1000)
		resultado = sorted(array)
		selectionSort(array)
		self.assertEqual(resultado, array)

	def test002OrdenarListaDe500ElementosInsertionSort(self):
		array = generarArrayRandom(500, 0, 1000)
		resultado = sorted(array)
		insertionSort(array)
		self.assertEqual(resultado, array)

	def test003OrdenarListaDe500ElementosQuickSort(self):
		array = generarArrayRandom(500, 0, 1000)
		resultado = sorted(array)
		arrayOrdenado = quickSort(array)
		self.assertEqual(resultado, arrayOrdenado)

	def test004OrdenarListaDe500ElementosheapSort(self):
		array = generarArrayRandom(500, 0, 1000)
		resultado = sorted(array)
		heapSort(array)
		self.assertEqual(resultado, array)

	def test005OrdenarListaDe500ElementosMergeSort(self):
		array = generarArrayRandom(500, 0, 1000)
		resultado = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(resultado, arrayOrdenado)

class TestListaDe1000Elementos(unittest.TestCase):

	def test001OrdenarListaDe1000ElementosSelectionSort(self):
		array = generarArrayRandom(1000, 0, 10000)
		resultado = sorted(array)
		selectionSort(array)
		self.assertEqual(resultado, array)

	def test002OrdenarListaDe1000ElementosElementosInsertionSort(self):
		array = generarArrayRandom(1000, 0, 10000)
		resultado = sorted(array)
		insertionSort(array)
		self.assertEqual(resultado, array)

	def test003OrdenarListaDe1000ElementosElementosQuickSort(self):
		array = generarArrayRandom(1000, 0, 10000)
		resultado = sorted(array)
		arrayOrdenado = quickSort(array)
		self.assertEqual(resultado, arrayOrdenado)

	def test004OrdenarListaDe1000ElementosElementosheapSort(self):
		array = generarArrayRandom(1000, 0, 10000)
		resultado = sorted(array)
		heapSort(array)
		self.assertEqual(resultado, array)

	def test005OrdenarListaDe1000ElementosElementosMergeSort(self):
		array = generarArrayRandom(1000, 0, 10000)
		resultado = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(resultado, arrayOrdenado)

class TestListaDe500ElementosNegativos(unittest.TestCase):

	def test001OrdenarListaDe500ElementosNegativosSelectionSort(self):
		array = generarArrayRandom(500, -1000, 0)
		resultado = sorted(array)
		selectionSort(array)
		self.assertEqual(resultado, array)

	def test002OrdenarListaDe500ElementosNegativosInsertionSort(self):
		array = generarArrayRandom(500, -1000, 0)
		resultado = sorted(array)
		insertionSort(array)
		self.assertEqual(resultado, array)

	def test003OrdenarListaDe500ElementosNegativosQuickSort(self):
		array = generarArrayRandom(500, -1000, 0)
		resultado = sorted(array)
		arrayOrdenado = quickSort(array)
		self.assertEqual(resultado, arrayOrdenado)

	def test004OrdenarListaDe500ElementosNegativosheapSort(self):
		array = generarArrayRandom(500, -1000, 0)
		resultado = sorted(array)
		heapSort(array)
		self.assertEqual(resultado, array)

	def test005OrdenarListaDe500ElementosNegativosMergeSort(self):
		array = generarArrayRandom(500, -1000, 0)
		resultado = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(resultado, arrayOrdenado)

class TestListaOrdenada(unittest.TestCase):

	def test001OrdenarListaOrdenadaSelectionSort(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		resultado = sorted(array)
		selectionSort(array)
		self.assertEqual(resultado, array)

	def test002OrdenarListaOrdenadaInsertionSort(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		resultado = sorted(array)
		insertionSort(array)
		self.assertEqual(resultado, array)

	def test003OrdenarListaOrdenadaQuickSort(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		resultado = sorted(array)
		arrayOrdenado = quickSort(array)
		self.assertEqual(resultado, arrayOrdenado)

	def test004OrdenarListaOrdenadaheapSort(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		resultado = sorted(array)
		heapSort(array)
		self.assertEqual(resultado, array)

	def test005OrdenarListaOrdenadaMergeSort(self):
		array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		resultado = sorted(array)
		arrayOrdenado = mergeSort(array)
		self.assertEqual(resultado, arrayOrdenado)

if __name__ == '__main__':
	unittest.main()
