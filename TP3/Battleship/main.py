import os
import CrearGrilla
from Juego import Juego
from VistaJuego import VistaJuego

DEFAULT_GRILLA = [5, 20, (500,1000), 300] # Filas, Columnas, Rango de Vida barco, maximo danio de celda
DEFAULT_LANZADERAS = 3
ARCHIVO = 'grilla.coords'

def main():
    archivo = ARCHIVO
    if not os.path.exists(archivo):
        archivo = CrearGrilla.crearArchivo(ARCHIVO, DEFAULT_GRILLA)

    matrizTablero = Juego.ArchivoToMatriz(archivo)
    barcos = Juego.ArchivoToBarcos(archivo)
    lanzaderas = Juego.CrearLanzaderas(DEFAULT_LANZADERAS)
    
    juego = Juego(matrizTablero, barcos, lanzaderas)
    vista = VistaJuego(juego)
    vista.imprimirLineas()

if __name__ == '__main__':
	main()