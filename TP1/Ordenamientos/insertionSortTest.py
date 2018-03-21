import unittest
from insertionSort import insertionSort
from generarArrayRandom import generarArrayRandom

class TestSelectionSort(unittest.TestCase):

    def test01OrdenarListaVacia(self):
        array = []
        result = []
        insertionSort(array)
        self.assertEqual(result, array)

    def test02OrdenarListaDe2Elementos(self):
        array = [2, 1]
        result = [1, 2]
        insertionSort(array)
        self.assertEqual(result, array)

    def test03OrdenarListaDe500Elementos(self):
        array = generarArrayRandom(500, 0, 1000)
        result = sorted(array)
        insertionSort(array)
        self.assertEqual(result, array)

    def test04OrdenarListaDe500ElementosNegativos(self):
        array = generarArrayRandom(500, -1000, 0)
        result = sorted(array)
        insertionSort(array)
        self.assertEqual(result, array)


if __name__ == '__main__':
    unittest.main()