class Barco():
    def __init__(self, vida):
        self.vida = vida
        self.posicion = None

    def atacar(self, danio):
        self.vida -= danio

    def estaDerribado(self):
        return self.vida <= 0

    def getPosicion(self):
        return self.posicion

    def setPosicion(self, x, y):
        self.posicion = (x, y)