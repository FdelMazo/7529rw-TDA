import unittest
from Barco import Barco

class TestBarcoDerribado(unittest.TestCase):
    def testBarcoDerribadoDanioJusto(self):
        barco = Barco(100)
        barco.recibirDanio(100)
        self.assertTrue(barco.estaDerribado())
        self.assertFalse(barco.getVida())

    def testBarcoDerribadoDanioDeMas(self):
        barco = Barco(10)
        barco.recibirDanio(1000)
        self.assertTrue(barco.estaDerribado())
        self.assertFalse(barco.getVida())

class TestBarcoNoDerribado(unittest.TestCase):
    def testBarcoNoEstaDerribado(self):
        barco = Barco(100)
        barco.recibirDanio(50)
        self.assertFalse(barco.estaDerribado())
        self.assertTrue(barco.getVida())

class TestPosicion(unittest.TestCase):
    def testPosicionEnYIgualAID(self):
        barco = Barco(100)
        barco.setPosicion(3,7)
        self.assertEqual(barco.getPosicion(), (3,7))
        self.assertEqual(barco.getPosicion()[1], barco.getID())
