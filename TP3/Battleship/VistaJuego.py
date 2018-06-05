class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class VistaJuego():
    def __init__(self, juego):
        self.juego = juego

    def imprimirFila(self, fila, y):
        linea = ""
        barco = self.juego.getBarcos()[y]
        xBarco = barco.getPosicion()[0]
        for x,n in enumerate(fila):
            if x == xBarco and not barco.estaDerribado(): 
                num = "<{}>".format(str(n).center(3))
                celda = "{}{}{}|".format(bcolors.GREEN,num,bcolors.ENDC)
            else: 
                num = "{}".format(n).center(5)
                celda = "{}|".format(num)
            linea+=celda
        stringBarco = "\t\t{} Barco {}: ".format(bcolors.RED, y)
        if barco.estaDerribado(): stringBarco+="Dead"
        else: stringBarco+="{}HP".format(barco.getVida())
        stringBarco+=bcolors.ENDC
        linea+= stringBarco
        print(linea)
        
    def informacionAdicional(self):
        string = "Turno: {}\n".format(self.juego.turno)
        string += "Puntos: {}\n".format(self.juego.puntos)
        barcosVivos = self.juego.getBarcosVivos()
        string += "Barcos en juego: {}\n".format(len(barcosVivos))
        for i,l in enumerate(self.juego.lanzaderas):
            string += "Lanzadera {} Target: {}\n".format(i, self.juego.targets[i])
        print(string)

    def update(self):
        print("*******************************")
        self.informacionAdicional()
        for columna, fila in enumerate(self.juego.matriz):
            self.imprimirFila(fila, columna)
        print()

    def start(self):
        string = "\n\n*******************************\n"
        string += "Battleship: La batalla final! \n"
        string += "*******************************\n\n"
        string += "En esta esquina, Dyno! El mejor programador de la historia desde Thomas Cormen \n"
        string += "En esta otra, Greedo! El sucesor al creador de la programacion greedy, John Greedy \n\n"
        string += "{} lanzaderas de misiles, {} barcos, y mucha, mucha, muuuuuuuucha acción\n\n".format(len(self.juego.lanzaderas),len(self.juego.getBarcos()))
        print(string)

    def end(self):
        string = "\n\n*******************************\n"
        string +=  "Turno finalizado!\n"
        string += "En {} turnos se alcanzaron {} puntos!\n".format(self.juego.turno, self.juego.puntos)
        string += "*******************************"
        print(string)

    @staticmethod
    def imprimirSeparacion():
        string = "\n*******************************\n"
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
