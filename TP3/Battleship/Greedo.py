class Greedo():
    def __init__(self):
        self.nombre = 'Greedo'  
    
    def turno(self, juego, barcos, lanzaderas):
        dic = {} #dic = {barco:danioCasillero}
        for barco in barcos:
            x, y = barco.getPosicion()
            dic[barco] = juego.getValorCasillero(x, y)
        barcosOrdenados = sorted(dic.items(), key=lambda x: x[1])
        barcosDisponibles = len(barcosOrdenados)
        barcoActual = barcosOrdenados[barcosDisponibles - 1]
        for i in range(len(lanzaderas)):
            barco, danio = barcoActual
            barco.atacar(danio)
            if barco.estaDerribado():
                barcosDisponibles -= 1
                juego.removerBarco(barco)
                if not juego.terminado():
                    barcoActual = barcosOrdenados[barcosDisponibles - 1]
                else:
                    break