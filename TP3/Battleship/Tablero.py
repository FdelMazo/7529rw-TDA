from Barco import *

class Tablero():
    def __init__(self, matriz, barcos, lanzaderas):
        self.matriz = matriz
        self.barcos = barcos
        self.lanzaderas = lanzaderas

    def avanzarBarcos(self):
        for barco in self.barcos:
            x, y = barco.getPosicion()
            if y == len(self.matriz[x]) - 1:
                barco.setPosicion(x, 0)
            else:
                barco.setPosicion(x, y + 1)

    def getCantidadDeLanzaderas(self):
        return self.lanzaderas

    def removerBarco(self, barco):
        if barco in self.barcos:
            self.barcos.remove(barco)