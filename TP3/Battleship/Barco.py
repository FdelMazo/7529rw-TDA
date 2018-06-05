class Barco():
    def __init__(self, vida):
        self.vida = vida
        self.posicion = None

    def recibirDanio(self, danio):
        self.vida -= danio
        if self.vida < 0: self.vida = 0

    def estaDerribado(self):
        return self.vida == 0

    def getPosicion(self):
        return self.posicion

    def setPosicion(self, x, y):
        self.posicion = (x, y)

    def getVida(self):
        return self.vida