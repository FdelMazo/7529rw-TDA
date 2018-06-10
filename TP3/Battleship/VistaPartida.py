
class VistaPartida():
	def __init__(self, partida, terminal):
		self.partida = partida
		self.terminal = terminal

	def start(self):
		string = "Comienza la partida de {}\n".format(self.partida.jugador)
		string += "{} lanzaderas de misiles, {} barcos\n".format(
					 self.partida.cantidadLanzaderas,
					 len(self.partida.getBarcos()))
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.clear()

	def imprimirMapa(self):
		digitos = 0
		for fila in self.partida.matriz:
			digitosFila = len(str(max(fila)))
			digitos = digitosFila if digitosFila>digitos else digitos
		for columna, fila in enumerate(self.partida.matriz):
			self.imprimirFila(fila, columna,digitos)
		print("*******************************\n")
		self.terminal.clear()

	def imprimirFila(self, fila, y, digitos):
		linea = ""
		barco = self.partida.getBarcos()[y]
		xBarco = barco.getPosicion()[0]
		for x, n in enumerate(fila):
			if x == xBarco and not barco.estaDerribado():
				num = "<{}>".format(str(n).rjust(digitos))
				celda = self.terminal.pretty_string(num, 'OK')
				celda += "|"
			else:
				num = "{}".format(n).center(digitos+2)
				celda = "{}|".format(num)
			linea += celda
		if barco.estaDerribado():
			stringBarco = self.terminal.pretty_string("\t\t {}: Destruído".format(barco),'NOT_OK')
		else:
			stringBarco = self.terminal.pretty_string("\t\t {}: {} HP".format(barco, barco.getVida()),'OK')
		linea += stringBarco
		print(linea)

	def informacionTurno(self):
		print("*******************************")
		string = "{}\n\n".format(self.partida)
		string += "Lanzaderas: {}\n".format(self.partida.getCantidadLanzaderas())
		string += "Barcos en juego: {}\n\n".format(len(self.partida.getBarcosVivos()))
		for i in range(self.partida.cantidadLanzaderas):
			if self.partida.targetDelTurno[i] != None and not self.partida.terminada():
				barco = self.partida.getBarcos()[self.partida.targetDelTurno[i]]
				stringDanioPotencial = "(Daño Potencial: {}HP)".format(self.partida.getDanioCasillero(*barco.getPosicion()))
			else:
				barco = None
				stringDanioPotencial = ""
			string += "Lanzadera {} --> {} {}\n".format(i, barco,stringDanioPotencial)
		print(string)

	def end(self):
		string = "*******************************\n" \
				"Turno finalizado\n" \
				"En {} turnos, peleando contra {}, el bando A alcanzó {} puntos\n".format(self.partida.turno, self.partida.jugador,
																self.partida.getPuntos())
		string += "*******************************\n"
		print(self.terminal.pretty_string(string,'TITLE'))
		self.terminal.clear()