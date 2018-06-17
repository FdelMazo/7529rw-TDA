import os
import platform

PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
CLEAR = "\033[H\033[J"

COLOR_SEGUN_FUNCION = {'OK': GREEN, 'NOT_OK': RED, 'TITLE': PURPLE}

class Terminal():
	"""Clase encargada del manejo de colores, limpiado de la terminal y separacion con teclado (input)
	En Linux se imprimen cadenas con colores
	En Linux y Windows se limpia la terminal
	No se puede asumir el comportamiento de cualquier otro OS"""

	def __init__(self, no_input):
		self.linux = True if platform.system() == 'Linux' else False
		self.windows = True if platform.system() == 'Windows' else False
		self.input = not no_input

	def pretty_string(self, s, funcion):
		if self.linux:
			string = "{}{}{}".format(
				COLOR_SEGUN_FUNCION[funcion],
				s,
				END)
		else: string = s
		return string

	def clear(self):
		if not self.input: return
		input()
		if self.linux: print(CLEAR)
		elif self.windows: os.system('cls')

	def print_avisar_input(self):
		if self.input: print(self.pretty_string('ENTER PARA CONTINUAR', 'TITLE'))