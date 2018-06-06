import random, argparse

FILAS = 5
COLUMNAS = 10
RANGE_VIDA = (500, 1000)
MAX_DANIO = 300

PARAMS = [FILAS, COLUMNAS, RANGE_VIDA, MAX_DANIO]

FILE = 'grilla.coords'

def crearTablero(cantFilas, columnas, vida, danio):
	filas = []
	for i in range(cantFilas):
		fila = []
		barco = random.randint(*vida)
		barco = round(barco, -2) # Redondea a la centena
		fila.append(barco)

		for i in range(columnas):
			celda = random.randint(0,danio)
			celda = round(celda, -1) # Redondea a la decena
			fila.append(celda)
 
		fila = ' '.join([str(x) for x in fila])
		filas.append(fila)
	return filas
	
def filasToArchivo(filas, archivo):
	with open(archivo, 'w') as f:
		f.write('\n'.join(filas))
	return archivo

def crearArchivo(archivo = FILE, params = PARAMS):
	filas = crearTablero(*params)
	archivo = filasToArchivo(filas, archivo)
	return archivo

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('filas', help='Cantidad de filas', type=int)
	parser.add_argument('columnas', help='Cantidad de columnas', type=int)
	parser.add_argument('vidamin', help='Mínima vida del barco', action='store', type=int)
	parser.add_argument('vidamax', help='Máxima vida del barco', action='store', type=int)
	parser.add_argument('max_danio', help='Máximo danio de las celdas', action='store', type=int)
	parser.add_argument('-f', '--file', help='Cambiar nombre de archivo', action='store', default=FILE)
	args = parser.parse_args()
	params = [args.filas, args.columnas, (args.vidamin, args.vidamax), args.max_danio]
	crearArchivo(args.file, params)