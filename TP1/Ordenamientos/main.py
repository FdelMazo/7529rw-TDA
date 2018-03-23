import argparse
import time

from generarArrayRandom import generarArrayRandom
from heapSort import heapSort
from mergeSort import mergeSort
from quickSort import quickSort
from insertionSort import insertionSort
from selectionSort import selectionSort

SORTS = {"heapSort":heapSort, "mergeSort":mergeSort, "quickSort":quickSort, "insertionSort":insertionSort, "selectionSort":selectionSort}

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('ordenamiento',help='Nombre del ordenamiento a ejecutar', nargs='?', action = 'store', default = None)
	parser.add_argument('cantidadElementos',help='Cantidad de elementos a ordenar', nargs='?', action = 'store', type=int, default = 10000)
	args = parser.parse_args()
	
	print("Ejecutando {} con {} elementos".format(args.ordenamiento, args.cantidadElementos))
	start_time = time.clock()
	array = generarArrayRandom(args.cantidadElementos, 0, args.cantidadElementos)		
	SORTS[args.ordenamiento](array)
	print("Tiempo final de ejecucion: {} segundos".format(time.clock() - start_time))

main()
