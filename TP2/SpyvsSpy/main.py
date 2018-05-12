from Grafo import *
from GrafoPesado import *
import os
from bfs import *
from Dijkstra import *
import ManejoDeArchivos
import argparse
import random

DIMENSION_DEFAULT = 50
PORCENTAJE_CARGA_DEFAULT = 70

def definirGanador(grafo, posiciones, pesado, sin_camino):
    espiaBlanco, espiaNegro, aeropuerto = posiciones
    
    if pesado:
        if sin_camino:
            distanciaBlanco = distanciaConPeso(grafo, espiaBlanco, aeropuerto)
            distanciaNegro = distanciaConPeso(grafo, espiaNegro, aeropuerto)
            return 'Negro' if distanciaNegro<distanciaBlanco else 'Blanco', []
        else:
            caminoBlanco = minimoCaminoConPeso(grafo, espiaBlanco, aeropuerto)
            caminoNegro = minimoCaminoConPeso(grafo, espiaNegro, aeropuerto)
            if len(caminoNegro)<len(caminoBlanco):
                return 'Negro', caminoNegro
            else:
                return 'Blanco', caminoBlanco
    else:
        if sin_camino:
            distanciaBlanco = distanciaSinPeso(grafo, espiaBlanco, aeropuerto)
            distanciaNegro = distanciaSinPeso(grafo, espiaNegro, aeropuerto)
            return 'Negro' if distanciaNegro<distanciaBlanco else 'Blanco', []
        else:
            caminoBlanco = minimoCaminoSinPeso(grafo, espiaBlanco, aeropuerto)
            caminoNegro = minimoCaminoSinPeso(grafo, espiaNegro, aeropuerto)
            if len(caminoNegro)<len(caminoBlanco):
                return 'Negro', caminoNegro
            else:
                return 'Blanco', caminoBlanco
                
def main():
    """Programa que dados dos espias y un objetivo final (aeropuerto), decide el que llega primero.
    ¿Quien recorre el camino mas corto?"""
    parser = argparse.ArgumentParser()
    parser.add_argument('coordenadas',
                        help='Lista de 3 numeros de linea de mapa.coords donde el primer vertice es la posicion del espia blanco, espia negro y el aeropuerto respectivamente.',
                        nargs='*', action='store')
    parser.add_argument('--pesado', help='Intercalar entre grafo pesado y no pesado', action='store_true')
    parser.add_argument('--sin-camino', help='Calcular y devolver el camino o solamente anunciar al ganador', action='store_true')
    args = parser.parse_args()

    if not os.path.isfile('mapa.coords'):
        print("Mapa no presente! Se genera el mapa default, de dimension {}x{}, un {} cargado".format(DIMENSION_DEFAULT, DIMENSION_DEFAULT, PORCENTAJE_CARGA_DEFAULT))
        ManejoDeArchivos.generarArchivo(DIMENSION_DEFAULT, DIMENSION_DEFAULT,PORCENTAJE_CARGA_DEFAULT)

    grafo = ManejoDeArchivos.crearGrafoDesdeArchivo(pesado=args.pesado)
    posiciones = ManejoDeArchivos.obtener_vertices(args.coordenadas)

    print(
        "Un espia blanco intenta escaparse desde {}\n".format(posiciones[0]) + 
        "Mientras que un espia negro intenta agarrarlo desde {}\n".format(posiciones[1]) +
        "¿Quien llegara antes al aeropuerto ubicado en {}?\n".format(posiciones[2])
    )

    ganador, camino = definirGanador(grafo, posiciones,args.pesado, args.sin_camino)

    if ganador == "Blanco":
        print("Gano el Espia Blanco! Llego a escaparse del pais antes de que lo atrape ese sucio Espia Negro.")
    else:
        print("Gano el Espia Negro! Obtuvo los documentos antes de que esa zarigüella blanca logre escaparse.")
    if camino: print("Su camino fue: {}".format(' -> '.join([str(x) for x in camino])))
    

if __name__ == '__main__':
    main()