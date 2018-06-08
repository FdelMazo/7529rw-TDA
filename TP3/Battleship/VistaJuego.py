from Terminal import Terminal
from VistaPartida import VistaPartida


class VistaJuego():
	def __init__(self, juego, no_input):
		self.juego = juego
		self.terminal = Terminal(no_input)

	def titulo(self):
		string = "\n*******************************\n" \
				 "Battleship: La Batalla Final! \n\n" \
				 "En esta esquina, el memorizador Dyno! El mejor programador de la historia desde Thomas Cormen \n" \
				 "En esta otra, el goloso Greedo! El sucesor al creador de la programacion greedy, John Greedy \n" \
				 "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.print_command()
		self.terminal.clear()

	def cambioDeTurno(self):
		string = "*******************************\n" \
				 "Cambio de turno!!!\n" \
				 "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))
		self.terminal.clear()

	def imprimirGanador(self):
		string = "*******************************\n"
		if self.juego.ganador: ganadorString = "El ganador es {}!!!\n".format(self.juego.ganador)
		else: ganadorString = "Empataron con {} puntos!!!\n".format(self.juego.jugadores[0].getPuntos())

		ganadorString += "{}: {} Puntos\n".format(self.juego.jugadores[0], self.juego.jugadores[0].getPuntos())
		ganadorString += "{}: {} Puntos\n".format(self.juego.jugadores[1], self.juego.jugadores[1].getPuntos())
		string += ganadorString
		string += "*******************************\n"
		print(self.terminal.pretty_string(string, 'TITLE'))

	def nuevaVistaPartida(self, partida):
		vistaPartida = VistaPartida(partida, self.terminal)
		return vistaPartida


