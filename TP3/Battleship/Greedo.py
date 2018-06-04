from Tablero import *
from Barco import *

def GreedoTurno(tablero, barcos, lanzaderas):
    dic = {} #dic = {barco:danioCasillero}
    for barco in barcos:
        x, y = barco.getPosicion()
        dic[barco] = tablero.getValorCasillero(x, y)
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

def Greedo(tablero):
    puntaje = 0
    while not tablero.estaVacio():
        barcos = tablero.getBarcos()
        lanzaderas = tablero.getCantidadDeLanzaderas()
        GreedoTurno(tablero, barcos, lanzaderas)
        puntaje += tablero.getCantidadDeBarcos()