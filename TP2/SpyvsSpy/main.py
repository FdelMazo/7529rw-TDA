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
        if sin_camino:
            distanciaBlanco = distanciaConPeso(grafo, espiaBlanco, aeropuerto)
            distanciaNegro = distanciaConPeso(grafo, espiaNegro, aeropuerto)
            if distanciaBlanco == -1 and distanciaNegro == -1: return '', 0
            elif distanciaBlanco == -1: return 'Negro', distanciaNegro
            elif distanciaNegro == -1: return 'Blanco', distanciaBlanco
            if distanciaNegro < distanciaBlanco:
                return 'Negro', distanciaNegro
            else:
                return 'Blanco', distanciaBlanco
        else:
            distanciaBlanco = distanciaConPeso(grafo, espiaBlanco, aeropuerto)
            distanciaNegro = distanciaConPeso(grafo, espiaNegro, aeropuerto)
            if distanciaBlanco == -1 and distanciaNegro == -1: return '', []
            elif distanciaBlanco == -1: return 'Negro', minimoCaminoConPeso(grafo, espiaNegro, aeropuerto)
            elif distanciaNegro == -1: return 'Blanco', minimoCaminoConPeso(grafo, espiaBlanco, aeropuerto)
            if distanciaNegro < distanciaBlanco:
                return 'Negro', minimoCaminoConPeso(grafo, espiaNegro, aeropuerto)
            else:
                return 'Blanco', minimoCaminoConPeso(grafo, espiaBlanco, aeropuerto)
    else:
        if sin_camino:
            distanciaBlanco = distanciaSinPeso(grafo, espiaBlanco, aeropuerto)
            distanciaNegro = distanciaSinPeso(grafo, espiaNegro, aeropuerto)
            if distanciaBlanco == -1 and distanciaNegro == -1: return '', 0
            elif distanciaBlanco == -1: return 'Negro', distanciaNegro
            elif distanciaNegro == -1: return 'Blanco', distanciaBlanco
            if distanciaNegro < distanciaBlanco:
                return 'Negro', distanciaNegro
            else:
                return 'Blanco', distanciaBlanco
        else:
            caminoBlanco = minimoCaminoSinPeso(grafo, espiaBlanco, aeropuerto)
            caminoNegro = minimoCaminoSinPeso(grafo, espiaNegro, aeropuerto)
            if not caminoBlanco and not caminoNegro: return '', []
            elif not caminoBlanco: return 'Negro', caminoNegro
            elif not caminoNegro: return 'Blanco', caminoBlanco
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
                        nargs='+', action='store')
    parser.add_argument('--pesado', help='Intercalar entre grafo pesado y no pesado', action='store_true')
    parser.add_argument('--sin-camino', help='Calcular y devolver el camino o solamente anunciar al ganador', action='store_true')
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

    ganador, camino_o_distancia = definirGanador(grafo, posiciones,args.pesado, args.sin_camino)
    if not ganador:
        print("No gano nadie :( \nAmbos espias no tienen camino al aeropuerto.")  
        return 
    if ganador == "Blanco":
        print("¡Ganó el Espía Blanco! Llego a escaparse del país antes de que lo atrape el Espia Negro.")
    else:
        print("¡Ganó el Espia Negro! Obtuvo los documentos antes de que el espía blanco logre escaparse.")  
    if isinstance(camino_o_distancia,list):
        print("Su camino fue: {}".format(' -> '.join([str(x) for x in camino_o_distancia])))
    elif isinstance(camino_o_distancia,(int,float)):
        print("Su distancia recorrida fue de: {:.2}".format(float(camino_o_distancia)))

if __name__ == '__main__':
    main()