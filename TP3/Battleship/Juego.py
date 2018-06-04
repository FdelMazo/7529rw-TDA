from Barco import *
from Lanzadera import *

class Juego():
    def __init__(self, matriz, barcos, lanzaderas):
        self.matriz = matriz
        self.barcos = barcos
        self.lanzaderas = lanzaderas

    def avanzarBarcos(self):
        for barco in self.barcos:
            x, y = barco.getPosicion()
            if x == len(self.matriz[y]) - 1:
                barco.setPosicion(y, 0)
            else:
                barco.setPosicion(y, x + 1)

    def removerBarco(self, barco):
        if barco in self.barcos:
            self.barcos.remove(barco)

    def estaVacio(self):
        return len(self.barcos) == 0

    def getCantidadDeLanzaderas(self):
        return self.lanzaderas

    def getBarcos(self):
        return self.barcos

    def getCantidadDeBarcos(self):
        return len(self.barcos)

    def getValorCasillero(self, x, y):
        return self.matriz[y][x]

    @staticmethod
    def ArchivoToBarcos(archivo):
        vida_barcos = []
        with open(archivo, 'r') as f:
            for linea in f:
                linea = linea.split()
                vida = int(linea[0])
                vida_barcos.append(vida)
        barcos = []
        for vida in vida_barcos:
            barcos.append(Barco(vida))
        return barcos

    @staticmethod
    def ArchivoToMatriz(archivo):
        matriz = []
        with open(archivo, 'r') as f:
            for linea in f:
                linea = linea.split()
                linea = linea[1:] #El primer valor es un barco
                linea = [int(x) for x in linea]
                matriz.append(linea)
        return matriz

    @staticmethod
    def CrearLanzaderas(cantidad):
        lanzaderas = []
        for x in range(cantidad):
            lanzaderas.append(Lanzadera())
        return lanzaderas