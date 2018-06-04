class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (bcolors.WARNING + "Warning: No active frommets remain. Continue?" 
      + bcolors.ENDC)

class VistaJuego():
    def __init__(self, juego):
        self.juego = juego

    def imprimirFila(self, fila, y):
        posBarcos = []
        for b in self.juego.getBarcos():
            posBarcos.append(b.getPosicion())
        for x,n in enumerate(fila):
            if (x,y) in posBarcos: 
                num = "<"+"{}".format(n).center(3)+">"
                celda = "{}{}{}|".format(bcolors.OKGREEN,num,bcolors.ENDC)
            else: 
                num = "{}".format(n).center(5)
                celda = "{}|".format(num)
            print(celda, end='')
        print()

    def informacionAdicional(self):
        string = "Turno: {}\n".format(self.juego.turno)
        string += "Puntos: {}\n".format(self.juego.puntos)
        barcosVivos = self.juego.getBarcos()
        string += "Barcos en juego: {}\n".format(len(barcosVivos))
        for i,b in enumerate(barcosVivos,1):
            string += "Barco {}: {}HP - {} daño potencial\n".format(
                i,
                b.getVida(),
                self.juego.getValorCasillero(*b.getPosicion())
            )
        for i,l in enumerate(self.juego.lanzaderas, 1):
            string += "Lanzadera {}: Target (???)\n".format(i)
        print(string)

    def update(self):
        for columna, fila in enumerate(self.juego.matriz):
            self.imprimirFila(fila, columna)
        print()
        self.informacionAdicional()

    def start(self):
        string = "\n\n*******************************\n"
        string += "Battleship: La batalla final! \n"
        string += "*******************************\n\n"
        string += "En esta esquina, Dyno! El mejor programador de la historia desde Thomas Cormen \n"
        string += "En esta otra, Greedo! El sucesor al creador de la programacion greedy, John Greedy \n\n"
        string += "{} lanzaderas de misiles, {} barcos, y mucha, mucha, muuuuuuuucha acción\n\n".format(len(self.juego.lanzaderas),len(self.juego.getBarcos()))
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
