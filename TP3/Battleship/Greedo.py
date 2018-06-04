from Tablero import *
from Barco import *

def GreedoTurno(tablero, matriz, barcos, lanzaderas):
    dic = {} #dic = {barco:danioCasillero}
    for barco in barcos:
        x, y = barco.getPosicion()
        dic[barco] = matriz[y][x]
    barcosOrdenados = sorted(dic.items(), key=lambda x: x[1])
    barcosDisponibles = len(barcosOrdenados)
    barcoActual = barcosOrdenados[barcosDisponibles - 1]
    for i in range(0, lanzaderas):
        barco, danio = barcoActual
        barco.atacar(danio)
        if barco.estaDerribado():
            barcosDisponibles -= 1
            tablero.removerBarco(barco)
            if not tablero.estaVacio():
                barcoActual = barcosOrdenados[barcosDisponibles - 1]
            else:
                break


[[1, 2, 3, 4],
 [6, 7, 8, 9],]