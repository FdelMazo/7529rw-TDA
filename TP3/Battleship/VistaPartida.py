
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
		for columna, fila in enumerate(self.partida.matriz):
			self.imprimirFila(fila, columna)
		print("*******************************\n")
		self.terminal.clear()

	def imprimirFila(self, fila, y):
		linea = ""
		barco = self.partida.getBarcos()[y]
		xBarco = barco.getPosicion()[0]
		for x, n in enumerate(fila):
			if x == xBarco and not barco.estaDerribado():
				num = "<{}>".format(str(n).center(3))
				celda = self.terminal.pretty_string(num, 'OK')
				celda += "|"
			else:
				num = "{}".format(n).center(5)
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
		string = "Jugador: {}\n".format(self.partida.jugador)
		string += "Turno: {}\n".format(self.partida.turno)
		string += "Puntos: {}\n".format(self.partida.jugador.getPuntos())
		string += "Lanzaderas: {}\n\n".format(self.partida.getCantidadLanzaderas())
		string += "Barcos en juego: {}\n\n".format(len(self.partida.getBarcosVivos()))
		for i in range(self.partida.cantidadLanzaderas):
			if self.partida.targetDelTurno[i] != None and not self.partida.terminada():
				coordenadas = (self.partida.turno, self.partida.targetDelTurno[i])
				stringBarco = "Barco {}".format(self.partida.targetDelTurno[i])
				stringDanioPotencial = "(Daño Potencial: {})".format(self.partida.getDanioCasillero(*coordenadas))
			else:
				stringBarco = "None"
				stringDanioPotencial = None
			string += "Lanzadera {} --> {} {}\n".format(i, stringBarco,stringDanioPotencial)
		print(string)

	def end(self):
		string = "*******************************\n" \
				"Turno finalizado\n" \
				"En {} turnos, {} alcanzó {} puntos\n".format(self.partida.turno, self.partida.jugador,
																self.partida.jugador.getPuntos())
		string += "*******************************\n"
		print(self.terminal.pretty_string(string,'TITLE'))
		self.terminal.clear()