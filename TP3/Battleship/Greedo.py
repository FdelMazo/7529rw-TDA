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
        targets = []
        for i in range(len(lanzaderas)):
            barco, danio = barcoActual
            dummyVida = barco.getVida()
            dummyVida -= danio
            targets.append(barco)
            if dummyVida <= 0:
                barcosDisponibles -= 1
                if barcosDisponibles == 0:
                    break
                barcoActual = barcosOrdenados[barcosDisponibles-1]
        return targets