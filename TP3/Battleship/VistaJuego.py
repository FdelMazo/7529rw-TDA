class VistaJuego():
    def __init__(self, juego):
        self.juego = juego

    def imprimirLinea(self, linea):
        for i in linea:
            num = "{}".format(i).center(5)
            celda = "{}|".format(num)
            print(celda, end='')
        print()

    def imprimirLineas(self):
        for linea in self.juego.matriz:
            self.imprimirLinea(linea)
