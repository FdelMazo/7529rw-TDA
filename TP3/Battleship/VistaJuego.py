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
	def __init__(self, juego, no_input):
		self.juego = juego
		self.input = not no_input

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
		if barco.estaDerribado():
			stringBarco = bcolors.RED
			stringBarco +="\t\t Barco {}: Dead".format(y)
		else:
			stringBarco = bcolors.GREEN
			stringBarco = "\t\t{} Barco {}: {} HP".format(bcolors.GREEN, y, barco.getVida())
		stringBarco+=bcolors.ENDC
		linea+= stringBarco
		print(linea)

	def informacionAdicional(self):
		print("*******************************")
		string = "Turno: {}\n".format(self.juego.turno)
		string += "Puntos: {}\n".format(self.juego.puntos)
		barcosVivos = self.juego.getBarcosVivos()
		string += "Barcos en juego: {}\n\n".format(len(barcosVivos))
		for i in range(self.juego.cantidadLanzaderas):
			if self.juego.barcosAtacados[i] and not self.juego.terminado():
				barco = "Barco {}".format(self.juego.barcosAtacados[i])
			else: barco = "None"
			string += "Lanzadera {} --> {}\n".format(i, barco)
		print(string)

	def update(self):
		for columna, fila in enumerate(self.juego.matriz):
			self.imprimirFila(fila, columna)
		print()
		if self.input: input()

	def start(self):
		string = "\n\n*******************************\n"
		string += "Battleship: La batalla final! \n"
		string += "*******************************\n\n"
		string += "En esta esquina, el memorizador Dyno! El mejor programador de la historia desde Thomas Cormen \n"
		string += "En esta otra, el goloso Greedo! El sucesor al creador de la programacion greedy, John Greedy \n\n"
		string += "{} lanzaderas de misiles, {} barcos, y mucha, mucha, muuuuuuuucha acción\n\n".format(self.juego.cantidadLanzaderas,len(self.juego.getBarcos()))
		print(string)
		if self.input: input("ENTER PARA PASAR DE TURNO\n")

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
