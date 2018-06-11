from Jugador import Jugador
from copy import deepcopy

class Dino(Jugador):

    def __init__(self):
        super().__init__('Dino')

    def devolverTuplasOrdenadasDanioTurnoBarco(self, partida):
        tuplas = []
        barcos = partida.getBarcos()
        matriz = partida.getMatriz()
        for barco in barcos:
            x, y = barco.getPosicion()
            fila = matriz[y]
            for i in range(0, len(fila)):
                danio = partida.getDanioCasillero(i, y)
                tupla = (danio, i, barco)
                tuplas.append(tupla)
        tuplas = sorted(tuplas, key=lambda x: x[0])
        return tuplas[::-1]

    def elegirTarget(self):
        tuplas = self.devolverTuplasOrdenadasDanioTurnoBarco(partida)
        barcoDanioAcumulado = {}
        turnosTargets = {}
        