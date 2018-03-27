import argparse
import time

from heapSort import heapSort
from mergeSort import mergeSort
from quickSort import quickSort
from insertionSort import insertionSort
from selectionSort import selectionSort

SORTS = [insertionSort, selectionSort, mergeSort, quickSort, heapSort]
CANTIDAD_ELEMENTOS = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]

def setALista(nombre_archivo, cantidadElementos):
	lista = []
	with open(nombre_archivo) as archivo:
		for linea, i  in zip(archivo,range(cantidadElementos)):
			lista.append(linea.strip())
	return lista

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('set',help='Nombre de archivo de set', nargs='?', action = 'store', default = "sets/set1.txt")
	args = parser.parse_args()

	for elementos in CANTIDAD_ELEMENTOS:
		print("\n\nComenzando ordenamientos sobre {} elementos\n".format(elementos))
		for ordenamiento in SORTS:
			print("Ejecutando {} con {} elementos del set '{}'".format(ordenamiento.__name__, elementos, args.set))
			start_time = time.process_time()
			lista = setALista(args.set, elementos)
			ordenamiento(lista)
			print("Tiempo final de ejecucion: {} segundos \n".format(time.process_time() - start_time))

main()
