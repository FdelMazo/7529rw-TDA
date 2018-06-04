from Barco import Barco
from Lanzadera import Lanzadera

class Juego():
    def __init__(self, matriz, barcos, lanzaderas):
        self.matriz = matriz
        self.barcos = barcos
        self.lanzaderas = lanzaderas
        self.turno = 0
        self.puntos = 0
        self.jugador = None
        self.setBarcos()
    
    def setBarcos(self):
        for i, b in enumerate(self.barcos):
            b.setPosicion(0,i)

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

    def getCantidadDeLanzaderas(self):
        return self.lanzaderas

    def getBarcos(self):
        return self.barcos

    def getCantidadDeBarcos(self):
        return len(self.barcos)

    def getValorCasillero(self, x, y):
        return self.matriz[y][x]

    def terminado(self):
        return not self.barcos

    def getPuntos(self):
        return self.puntos
    
    def setJugador(self,jugador):
        self.jugador = jugador

    def jugar(self):
        self.jugador.turno(self, self.barcos, self.lanzaderas)
        self.puntos += len(self.getBarcos())
        self.turno+=1

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