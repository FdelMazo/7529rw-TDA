from Grafo import *
from GrafoPesado import *
import os
from bfs import *
from Dijkstra import *
import ManejoDeArchivos
import argparse
import random

def definirGanador(grafo, posiciones, pesado, sin_camino):
    espiaBlanco, espiaNegro, aeropuerto = posiciones

    if pesado:
        distanciaBlanco = distanciaConPeso(grafo, espiaBlanco, aeropuerto)
        distanciaNegro = distanciaConPeso(grafo, espiaNegro, aeropuerto)
    else:
        distanciaBlanco = distanciaSinPeso(grafo, espiaBlanco, aeropuerto)
        distanciaNegro = distanciaSinPeso(grafo, espiaNegro, aeropuerto)

    if distanciaBlanco == -1 and distanciaNegro == -1: return '', None, None

    if distanciaBlanco == -1:
        ganador = 'Negro'
    elif distanciaNegro == -1:
        ganador = 'Blanco'
    else:
        ganador = 'Negro' if distanciaNegro < distanciaBlanco else 'Blanco'

    if sin_camino:
        return ganador, distanciaBlanco, distanciaNegro
    else:
        if pesado:
            return ganador, minimoCaminoConPeso(grafo, espiaBlanco, aeropuerto), minimoCaminoConPeso(grafo, espiaNegro, aeropuerto)
        else:
            return ganador, minimoCaminoSinPeso(grafo, espiaBlanco, aeropuerto), minimoCaminoSinPeso(grafo, espiaNegro, aeropuerto)

def imprimirGanador(ganador, blanco, negro):
    if not ganador:
        print("No ganó nadie \nNingún espía no tienen camino al aeropuerto.")
        return
    if ganador == "Blanco":
        print("¡Ganó el Espía Blanco! Llegó a escaparse del país antes de que lo atrape el Espía Negro.")
    else:
        print("¡Ganó el Espía Negro! Obtuvo los documentos antes de que el espía blanco logre escaparse.")
    if isinstance(blanco, list):
        if len(blanco) == 0:
            print("El espía blanco no tiene camino al aeropuerto")
        else:
            print("El camino del espía blanco fue: {}".format(' -> '.join([str(x) for x in blanco])))
    if isinstance(negro, list):
        if len(negro) == 0:
            print("El espía negro no tiene camino al aeropuerto")
        else:
            print("El camino del espia negro fue: {}".format(' -> '.join([str(x) for x in negro])))
    if isinstance(blanco,(int,float)):
        if blanco >= 0:
            print("La distancia recorrida del espia blanco fue de: {:.2}".format(float(blanco)))
        else:
            print("El espía blanco no tiene camino al aeropuerto")
    if isinstance(negro,(int,float)):
        if negro >= 0:
            print("La distancia recorrida del espaa negro fue de: {:.2}".format(float(negro)))
        else:
            print("El espía negro no tiene camino al aeropuerto")

def main():
    """Programa que dados dos espias y un objetivo final (aeropuerto), decide el que llega primero.
    ¿Quien recorre el camino mas corto?"""
    parser = argparse.ArgumentParser()
    parser.add_argument('coordenadas',
                        help='Lista de 3 numeros de linea de mapa.coords donde el primer vertice es la posicion del espia blanco, espia negro y el aeropuerto respectivamente.',
                        nargs='+', action='store')
    parser.add_argument('--pesado', help='Intercalar entre grafo pesado y no pesado', action='store_true')
    parser.add_argument('--sin-camino', help='Calcular y devolver el camino o solamente anunciar al ganador',
                        action='store_true')
    args = parser.parse_args()

    if not os.path.isfile('mapa.coords'):
        raise IOError("¡Mapa no presente! Crear un mapa con el archivo ManejoDeArchivos.py")

    if len(args.coordenadas) < 3:
        raise ValueError("3 numeros de linea deben ser dados. Ni más ni menos.")

    grafo = ManejoDeArchivos.crearGrafoDesdeArchivo(pesado=args.pesado)
    args.coordenadas = [int(x) for x in args.coordenadas]
    posiciones = ManejoDeArchivos.lineas_a_vertices(args.coordenadas)

    print(
        "Un espia blanco intenta escaparse desde {}\n".format(posiciones[0]) +
        "Mientras que un espia negro intenta agarrarlo desde {}\n".format(posiciones[1]) +
        "¿Quien llegara antes al aeropuerto ubicado en {}?\n".format(posiciones[2])
    )

    ganador, blanco, negro = definirGanador(grafo, posiciones, args.pesado, args.sin_camino)

    imprimirGanador(ganador, blanco, negro)

if __name__ == '__main__':
    main()
