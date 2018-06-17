from Terminal import Terminal
from VistaPartida import VistaPartida

class VistaJuego():
	"""Clase encargada de mostrar el juego. Es decir, un conjunto de partidas con distintos jugadores"""
	def __init__(self, juego, no_input):
		self.juego = juego
		self.terminal = Terminal(no_input)

	def titulo(self):
		string = "\n*******************************\n" \
				 "Battleship \n" \
				 "*******************************\n"

		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.print_avisar_input()
		self.terminal.clear()

	def cambioDeTurno(self):
		string = "*******************************\n" \
				 "Cambio de turno\n" \
				 "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.clear()

	def imprimirGanador(self):
		leaderboard = sorted(self.juego.partidas, key=lambda x: x.getPuntos())
		string = "*******************************\n"
		if len(leaderboard) == 1 or leaderboard[0].getPuntos() < leaderboard[1].getPuntos():
			ganadorString = "El ganador es {}\n\n".format(leaderboard[0].getJugador())
		else:
			ganadorString = "Empataron\n\n"
		string += ganadorString
		string += "Puntajes: \n"
		for partida in leaderboard:
			string += "  {}\n".format(partida)
		string += "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))

	def nuevaVistaPartida(self, partida):
		vistaPartida = VistaPartida(partida, self.terminal)
		return vistaPartida


