from Barco import *

class Tablero():
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