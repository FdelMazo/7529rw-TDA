import argparse
import time
import sys, os

from heapSort import heapSort
from mergeSort import mergeSort
from quickSort import quickSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from manejoDeArchivos import *

SORTS = [insertionSort, selectionSort, mergeSort, quickSort, heapSort]
CANTIDAD_ELEMENTOS = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]
DIRECTORIO_SETS = "sets/"

def calcularTiempoEjecucion(ordenamiento, lista):
    start_time = time.process_time()
    ordenamiento(lista)
    return time.process_time() - start_time

def imprimirTiempoEjecucion(diccionarioSets, set, resultados):
    for elementos in CANTIDAD_ELEMENTOS:
        print("Comenzando ordenamientos sobre {} elementos\n".format(elementos))
        for ordenamiento in SORTS:
            print("Ejecutando {} con {} elementos del set '{}'".format(ordenamiento.__name__, elementos, set))
            lista = diccionarioSets[set][:elementos]
            tiempo = calcularTiempoEjecucion(ordenamiento, lista)
            actualizarDiccionarioResultados(resultados, set, elementos, ordenamiento.__name__, tiempo)
            print("Tiempo final de ejecucion: {} segundos \n".format(tiempo))
        print("\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('caso', help='Caso a calcular (al azar, o peor caso)', nargs='?',
        choices = ["Random", "Peor"], action='store', default="Random")
    args = parser.parse_args()

    sys.setrecursionlimit(10000) # Necesario para el peor caso de quicksort

    diccionarioSets, resultados = {}, {}
    sets = sorted([s for s in os.listdir(DIRECTORIO_SETS) if args.caso in s])
    for s in sets: diccionarioSets[s] = setALista(os.path.join(DIRECTORIO_SETS,s))

    for set in sorted(diccionarioSets):
        imprimirTiempoEjecucion(diccionarioSets, set, resultados)
    exportCSV(resultados, sets, args.caso)

main()
