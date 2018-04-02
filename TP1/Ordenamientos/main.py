import argparse
import time
import sys

from heapSort import heapSort
from mergeSort import mergeSort
from quickSort import quickSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from manejoDeArchivos import setALista, rutasPorPalabra, rutaASet, rutasASet, exportCSV

SORTS = [(insertionSort, "insertionSort"), (selectionSort, "selectionSort"), (mergeSort, "mergeSort"), (quickSort, "quickSort"), (heapSort, "heapSort")]
CANTIDAD_ELEMENTOS = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]

def obtenerTiempoDeEjecucionDelOrdenamiento(ordenamiento, lista):
    """Recibe la funcion del ordenamiento y una lista de ints.
    Devuelve el tiempo de ejecucion en segundos de dicho ordenamiento sobre la lista."""
    start_time = time.process_time()
    ordenamiento(lista)
    tiempo = time.process_time() - start_time
    return tiempo

def imprimirTiempoDeEjecucionDelOrdenamiento(setNombre, setDic, archivosDic):
    """Recibe el nombre del set, el diccionario con los datos de todos los set y el diccionario
    en el que se almacenan los tiempos de la cantidad de elementos con los que se corrieron cada ordenamiento."""
    for elementos in CANTIDAD_ELEMENTOS:
        print("\n\nComenzando ordenamientos sobre {} elementos\n".format(elementos))
        for ordenamiento in SORTS:
            print("Ejecutando {} con {} elementos del set '{}'".format(ordenamiento[0].__name__, elementos, setNombre))
            lista = setDic[setNombre]
            tiempo = obtenerTiempoDeEjecucionDelOrdenamiento(ordenamiento[0], lista[:elementos])
            actualizarDiccionario(archivosDic, setNombre, elementos, ordenamiento[1], tiempo)
            print("Tiempo final de ejecucion: {} segundos \n".format(tiempo))

def actualizarDiccionario(dic, setNombre, elementos, ordenamientoNombre, tiempo):
    """Recibe: diccionario, el nombre del set, los elementos del set, el nombre del ordenamiento y el tiempo que tardo
    ejecucion con el set y la cantidad nombrada anteriormente."""
    dic[elementos] = dic.get(elementos, {})
    dic[elementos][setNombre] = dic[elementos].get(setNombre, {})
    dic[elementos][setNombre][ordenamientoNombre] = tiempo

def crearDiccionarioDeSets(set):
    """Recibe el nombre clave que representa a los sets.
    Crea un diccionario donde la clave es el nombre del set y el valor la lista de numeros"""
    dic = {}
    listaRutas = rutasPorPalabra(set)
    for setRuta in listaRutas:
        nombreSet = rutaASet(setRuta)
        arraySet = setALista(setRuta, 10000)
        dic[nombreSet] = arraySet
    return dic

def main():
    '''	parser = argparse.ArgumentParser()
    parser.add_argument('set',help='Nombre de archivo de set', nargs='?', action = 'store', default = "sets/set1.txt")
    args = parser.parse_args()
    '''
    sys.setrecursionlimit(10000)
    setDic = crearDiccionarioDeSets("set")
    peoresCasosDic = crearDiccionarioDeSets("descendente")
    setArchivosDic = {}
    peoresCasosArchivosDic = {}
    for setNombre in sorted(setDic):
        imprimirTiempoDeEjecucionDelOrdenamiento(setNombre, setDic, setArchivosDic)
    for setNombre in sorted(peoresCasosDic):
        imprimirTiempoDeEjecucionDelOrdenamiento(setNombre, peoresCasosDic, peoresCasosArchivosDic)
    exportCSV(setArchivosDic, sorted(rutasPorPalabra("set")), "estadisticas")
    exportCSV(peoresCasosArchivosDic, sorted(rutasPorPalabra("descendente")), "peoresCasos")

main()
