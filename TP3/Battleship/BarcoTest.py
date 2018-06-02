import unittest
from Barco import *

class TestBarcoDerribado(unittest.TestCase):
    def test1BarcoDerribado(self):
        barco = Barco(100)
        barco.atacar(100)
        self.assertTrue(barco.estaDerribado())

    def test2BarcoDerribado(self):
        barco = Barco(10)
        barco.atacar(1000)
        self.assertTrue(barco.estaDerribado())


class TestBarcoNoEstaDerribado(unittest.TestCase):
    def testBarcoNoEstaDerribado(self):
        barco = Barco(100)
        barco.atacar(50)
        self.assertFalse(barco.estaDerribado())
