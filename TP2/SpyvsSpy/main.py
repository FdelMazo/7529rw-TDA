from Grafo import *
from GrafoPesado import *
import os
from bfs import *
from Dijkstra import *
import ManejoDeArchivos
import argparse

def main():
    """Programa que dados dos espias y un objetivo final (aeropuerto), decide el que llega primero.
    ¿Quien recorre el camino mas corto?"""
    parser = argparse.ArgumentParser()
    parser.add_argument('coordenadas',help='Lista de 6 posiciones de los espias y el aerouperto.', nargs='*', action = 'store')
    parser.add_argument('--pesado', help='Intercalar entre grafo pesado y no pesado', action='store_true')
    args = parser.parse_args()

    args.coordenadas = [int (x) for x in args.coordenadas]
    if not os.path.isfile('mapa.coords'): 
        raise IOError("Mapa no presente! Ver `ManejoDeArchivos.py`")
    if len(args.coordenadas) != 6:
        raise ValueError("6 coordenadas deben ser dadas. Espia Blanco en X e Y, Espia negro en X e Y, Aeropuerto en X e Y")

    grafo = ManejoDeArchivos.crearGrafoDesdeArchivo(pesado=args.pesado)
    espiaBlanco, espiaNegro, aeropuerto = tuple(args.coordenadas[:2]), tuple(args.coordenadas[2:4]), tuple(args.coordenadas[4:6])
    
    if espiaBlanco not in grafo or espiaNegro not in grafo or aeropuerto not in grafo:
        raise ValueError("Las coordenadas introducidas no corresponden a 3 puntos del mapa")

    if args.pesado:
        caminoBlanco, distanciaBlanco = minimoCaminoConPeso(grafo, espiaBlanco, aeropuerto)
        caminoNegro, distanciaNegro = minimoCaminoConPeso(grafo, espiaNegro, aeropuerto)
    else:
        caminoBlanco, distanciaBlanco = minimoCaminoSinPesos(grafo, espiaBlanco, aeropuerto), []
        caminoNegro, distanciaNegro = minimoCaminoSinPesos(grafo, espiaNegro, aeropuerto), []

    if len(caminoBlanco) < len(caminoNegro):
        ganador = "Blanco"
    elif len(caminoNegro) < len(caminoBlanco):
        ganador = "Negro"
    else:
        ganador = "Empate"

    if ganador == "Blanco":
        print("Gano el Espia Blanco! Llego a escaparse del pais antes de que lo atrape ese sucio Espia Negro.")
        print("Su camino fue: {}".format(' -> '.join([str(x) for x in caminoBlanco])))
        if distanciaBlanco: 
            print("Con pesos: {}".format(' -> '.join([str(x) for x in distanciaBlanco])))

    elif ganador == "Negro":
        print("Gano el Espia Negro! Obtuvo los documentos antes de que esa zarigüella blanca logre escaparse.")
        print("Su camino fue: {}".format(' -> '.join([str(x) for x in caminoNegro])))
        if distanciaNegro: 
            print("Con pesos: {}".format(' -> '.join([str(round(x,2)) for x in distanciaNegro])))
     
    elif ganador == "Empate":
        print("Empataron! El espía blanco llego tan rápido al aeropuerto como el espía negro. Su unica opción fue agarrarse a las trompadas hasta que no se dieron cuenta y los documentos se volaron!")

    print("feed me more code")



if __name__ == '__main__':
    main()