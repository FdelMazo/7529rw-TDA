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
        turnosCantidad = len(partida.getMatriz()[0])
        #Lleno el diccionario de turnosTargets con el numero de turno y una lista vacia
        for i in range(0, turnosCantidad):
            turnosTargets[i] = []
        for tupla in tuplas:
            danio, turno, barco = tupla
            #si el turno no tiene ningun candidato o posee lanzaderas sin usar
            if len(turnosTargets[turno]) <= partida.cantidadLanzaderas:
                turnosTargets[turno] = turnosTargets.get(turno, []) + [tupla]
                barcoDanioAcumulado[barco] = barcoDanioAcumulado.get(barco, 0) + danio
            else:
                decidirMejorOpcion(tupla, turnosTargets, barcoDanioAcumulado)

    def decidirMejorOpcion(self, tuplaActual, turnosTargets, barcoDanioAcumulado):
        danioActual, turno, barcoActual = tuplaActual
        for tupla in turnosTargets[turno]:
            danio, turno, barco = tupla
            #Compruebo si al agregar esta tupla el barco actual se destruye

            #Compruebo que barco le falta menos para ser destruido
            #Si la tupla es mayor, entonces la cambio por la actual

            