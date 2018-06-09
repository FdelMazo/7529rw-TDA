from Terminal import Terminal
from VistaPartida import VistaPartida


class VistaJuego():
	def __init__(self, juego, no_input):
		self.juego = juego
		self.terminal = Terminal(no_input)

	def titulo(self):
		string = "\n*******************************\n" \
				 "Battleship \n\n" \
				 "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.print_command()
		self.terminal.clear()

	def cambioDeTurno(self):
		string = "*******************************\n" \
				 "Cambio de turno\n" \
				 "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.clear()

	def imprimirGanador(self):
		string = "*******************************\n"
		if self.juego.getLeaderboard()[0].getPuntos() == self.juego.getLeaderboard()[1].getPuntos():
			ganadorString = "Empataron\n\n"
		else:
			ganadorString = "El ganador es {}\n\n".format(self.juego.getLeaderboard()[0])
		string += ganadorString
		for j in self.juego.getLeaderboard():
			string += "{}: {} Puntos\n".format(j, j.getPuntos())
		string += "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))

	def nuevaVistaPartida(self, partida):
		vistaPartida = VistaPartida(partida, self.terminal)
		return vistaPartida


