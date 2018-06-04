class VistaJuego():
    def __init__(self, juego):
        self.juego = juego

    def imprimirLinea(self, linea):
        for i in linea:
            num = "{}".format(i).center(5)
            celda = "{}|".format(num)
            print(celda, end='')
        print()

    def informacionAdicional(self):
        string = "Turno: {}\n".format(self.juego.turno)
        string += "Puntos: {}\n".format(self.juego.puntos)
        barcosVivos = self.juego.getBarcosVivos()
        string += "Barcos en juego: {}\n".format(len(barcosVivos))
        for i,b in enumerate(barcosVivos,1):
            string += "Barco {}: {}HP - {} daño potencial\n".format(
                i,
                b.getVida(),
                self.juego.getValorCasillero(*b.getPosicion())
            )
        for i,l in enumerate(self.juego.lanzaderas, 1):
            string += "Lanzadera {}: Target ({})\n".format(i, l.getTarget())
        print(string)

    def update(self):
        for linea in self.juego.matriz:
            self.imprimirLinea(linea)
        print()

        #self.informacionAdicional()

    def start(self):
        string = "\n\n*******************************\n"
        string += "Battleship: La batalla final! \n"
        string += "*******************************\n\n"
        string += "En esta esquina, Dyno! El mejor programador de la historia desde Thomas Cormen \n"
        string += "En esta otra, Greedo! El sucesor al creador de la programacion greedy, John Greedy \n\n"
        string += "{} lanzaderas de misiles, {} barcos, y mucha, mucha, muuuuuuuucha acción\n\n".format(len(self.juego.barcos),len(self.juego.lanzaderas))
        print(string)

    def end(self):
        string =  "Turno finalizado!\n"
        string += "En {} turnos se alcanzaron {} puntos!".format(self.juego.turno, self.juego.puntos)
        print(string)

    @staticmethod
    def imprimirSeparacion():
        string = "\n\n*******************************\n"
        string += "Cambio de turno!!! \n"
        string += "*******************************\n\n"
        print(string)
    
    @staticmethod    
    def imprimirGanador(puntosGreedo, puntosDyno):
        ganador = "Greedo" if puntosGreedo<puntosDyno else "Dyno"      
        string = "\n\n*******************************\n"
        string += "El ganador es {}!!!\n".format(ganador)
        string += "*******************************\n\n"
        print(string)
