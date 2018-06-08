class Barco():
	def __init__(self, vida):
		self.vida = vida
		self.x = None
		self.y = None # La fila en la que se encuentra es equivalente al ID del barco (barco en fila 3 --> Barco 3)

	def recibirDanio(self, danio):
		self.vida -= danio
		if self.vida < 0: self.vida = 0

	def estaDerribado(self):
		return self.vida == 0

	def getPosicion(self):
		return self.x, self.y

	def setPosicion(self, x, y):
		self.x, self.y = x, y

	def getVida(self):
		return self.vida