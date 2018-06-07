import os


class VistaJuego():
    def __init__(self, juego, no_input, nombre_sistema):
        self.juego = juego
        self.input = not no_input
        self.linux = True if nombre_sistema == 'Linux' else False

    def start(self):
        string = "Comienza la partida de {}\n".format(self.juego.jugador)
        string += "{} lanzaderas de misiles, {} barcos, y mucha, mucha, muuuuuuuucha acción\n".format(
            self.juego.cantidadLanzaderas, len(self.juego.getBarcos()))
        print(string)
        if self.input: input("ENTER PARA PASAR DE TURNO\n")

    def imprimirMapa(self):
        for columna, fila in enumerate(self.juego.matriz):
            self.imprimirFila(fila, columna)
        print()
        if self.input: input()

    def imprimirFila(self, fila, y):
        linea = ""
        barco = self.juego.getBarcos()[y]
        xBarco = barco.getPosicion()[0]
        for x, n in enumerate(fila):
            if x == xBarco and not barco.estaDerribado():
                num = "<{}>".format(str(n).center(3))
                celda = ""
                if self.linux: celda += bcolors.GREEN
                celda += num
                if self.linux: celda += bcolors.END
                celda += "|"

            else:
                num = "{}".format(n).center(5)
                celda = "{}|".format(num)
            linea += celda
        stringBarco = ""
        if barco.estaDerribado():
            if self.linux: stringBarco += bcolors.RED
            stringBarco += "\t\t Barco {}: Dead".format(y)
        else:
            if self.linux: stringBarco += bcolors.GREEN
            stringBarco += "\t\t Barco {}: {} HP".format(y, barco.getVida())
        if self.linux: stringBarco += bcolors.END
        linea += stringBarco
        print(linea)

    def informacionTurno(self):
        if self.linux:
            print("\033[H\033[J")
        else:
            os.system('cls||clear')
        print("*******************************")
        string = "Turno: {}\n".format(self.juego.turno)
        string += "Puntos: {}\n".format(self.juego.jugador.getPuntos())
        string += "Lanzaderas: {}\n\n".format(self.juego.getCantidadLanzaderas())
        string += "Barcos en juego: {}\n\n".format(len(self.juego.getBarcosVivos()))
        for i in range(self.juego.cantidadLanzaderas):
            if self.juego.targets[i] != None and not self.juego.terminado():
                barco = "Barco {}".format(self.juego.targets[i])
            else:
                barco = "None"
            string += "Lanzadera {} --> {}\n".format(i, barco)
        print(string)

    def end(self):
        string = ""
        if self.linux: string += bcolors.PURPLE
        string += "\n\n*******************************\n"
        string += "Turno finalizado!\n"
        string += "En {} turnos, {} alcanzó {} puntos!\n".format(self.juego.turno, self.juego.jugador,
                                                                 self.juego.jugador.getPuntos())
        string += "*******************************"
        if self.linux: string += bcolors.END
        print(string)
        if self.input: input()

    @staticmethod
    def titulo(sistema):
        string = ""
        if sistema == "Linux": string += bcolors.PURPLE
        string += "\n\n*******************************\n"
        string += "Battleship: La Batalla Final! \n\n"
        string += "En esta esquina, el memorizador Dyno! El mejor programador de la historia desde Thomas Cormen \n"
        string += "En esta otra, el goloso Greedo! El sucesor al creador de la programacion greedy, John Greedy \n"
        string += "*******************************\n\n"
        if sistema == "Linux": string += bcolors.END
        print(string)

    @staticmethod
    def imprimirSeparacion(sistema):
        if sistema == "Linux":
            print("\033[H\033[J")
        else:
            os.system('cls||clear')
        string = ""
        if sistema == "Linux": string += bcolors.PURPLE
        string += "\n*******************************\n"
        string += "Cambio de turno!!!\n"
        string += "*******************************\n\n"
        if sistema == "Linux": string += bcolors.END
        print(string)

    @staticmethod
    def imprimirGanador(jugador1, jugador2, sistema):
        if sistema == "Linux":
            print("\033[H\033[J")
        else:
            os.system('cls||clear')
        if jugador1.getPuntos() < jugador2.getPuntos():
            ganador = jugador1
            perdedor = jugador2
        elif jugador2.getPuntos() < jugador1.getPuntos():
            ganador = jugador2
            perdedor = jugador1
        else:
            ganador, perdedor = '', ''
        string = ""
        if sistema == "Linux": string += bcolors.PURPLE
        string += "\n\n*******************************\n"
        if ganador:
            ganadorString = "El ganador es {}!!!\n".format(ganador)
            ganadorString += "Vencio con {} puntos versus los {} de su patético rival !!!\n".format(ganador.getPuntos(),
                                                                                                    perdedor.getPuntos())
        else:
            ganadorString = "Empataron con {} puntos!!!\n".format(jugador1.getPuntos())
        string += ganadorString
        string += "*******************************\n\n"
        if sistema == "Linux": string += bcolors.END
        print(string)


class bcolors:
    # Uso: bcolors.GREEN + "cadena" + bcolors.ENDC
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
