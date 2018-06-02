import unittest
from Barco import *

class TestBarcoDerribado(unittest.TestCase):
    def testBarcoDerribado(self):
        barco = Barco(100)
        barco.atacar(100)
        self.assertTrue(barco.estaDerribado())

class TestBarcoNoEstaDerribado(unittest.TestCase):
    def testBarcoNoEstaDerribado(self):
        barco = Barco(100)
        barco.atacar(50)
        self.assertFalse(barco.estaDerribado())