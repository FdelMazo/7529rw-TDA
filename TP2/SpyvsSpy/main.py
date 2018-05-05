from Grafo import *
from GrafoPesado import *
import os
from bfs import *
from Dijkstra import *
import ManejoDeArchivos
import argparse

DIMENSION_DEFAULT = 10
VERTICES_DEFAULT = 0.7

def main():
    """Programa que dados dos espias y un objetivo final (aeropuerto), decide el que llega primero.
    ¿Quien recorre el camino mas corto?"""
    parser = argparse.ArgumentParser()
    parser.add_argument('coordenadas',help='Lista de 3 numeros de linea de mapa.coords donde el primer vertice es la posicion del espia blanco, espia negro y el aeropuerto respectivamente.', nargs='*', action = 'store')
    parser.add_argument('--pesado', help='Intercalar entre grafo pesado y no pesado', action='store_true')
    args = parser.parse_args()

    if not os.path.isfile('mapa.coords'): 
        print("Mapa no presente! Se genera el mapa default, de dimension {}x{}, con {} vertices\n".format(DIMENSION_DEFAULT,DIMENSION_DEFAULT,VERTICES_DEFAULT*(DIMENSION_DEFAULT**2)))
        ManejoDeArchivos.generarArchivo(DIMENSION_DEFAULT,DIMENSION_DEFAULT,VERTICES_DEFAULT*(DIMENSION_DEFAULT**2))
    
    if not args.coordenadas: 
        print("Programa corrido sin parametros. Posiciones elegidas al azar\n")
        args.coordenadas = ManejoDeArchivos.elegirTresLineasAlAzar()
    
    args.coordenadas = ManejoDeArchivos.lineasToVertices(args.coordenadas)
   
    if len(args.coordenadas) != 3:
        raise ValueError("3 numeros de linea deben ser dados deben ser dadas")

    grafo = ManejoDeArchivos.crearGrafoDesdeArchivo(pesado=args.pesado)
    espiaBlanco, espiaNegro, aeropuerto = args.coordenadas

    print(
        "En una ciudad con {} puntos habiles para moverse\n".format(ManejoDeArchivos.cantidad_lineas()) +
        "Un espia blanco intenta escaparse desde {}\n".format(espiaBlanco) + 
        "Mientras que un espia negro intenta agarrarlo desde {}\n".format(espiaNegro) +
        "¿Quien llegara antes al aeropuerto ubicado en {}?\n".format(aeropuerto)
    )
    
    
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

if __name__ == '__main__':
    main()