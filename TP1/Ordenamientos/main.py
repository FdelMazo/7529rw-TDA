import argparse
import time
import os

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

def rutasPorPalabra(palabra):
	'''Recibe una palabra por parametro y devuelve las rutas (en una lista) de los archivos cuyo nombre contenga a dicha palabra '''
	lista_rutas = []
	for origen, carpetas, contenido in os.walk('.'):
		for archivo in contenido:
			if palabra in archivo:
				lista_rutas.append((os.path.join(origen, archivo)))
	return lista_rutas

def main():
	lista_rutas = rutasPorPalabra("set")
	for ruta_set in lista_rutas:
		for elementos in CANTIDAD_ELEMENTOS:
			print("\n\nComenzando ordenamientos sobre {} elementos\n".format(elementos))
			for ordenamiento in SORTS:
				print("Ejecutando {} con {} elementos del set '{}'".format(ordenamiento.__name__, elementos, ruta_set))
				start_time = time.process_time()
				lista = setALista(ruta_set, elementos)
				ordenamiento(lista)
				print("Tiempo final de ejecucion: {} segundos \n".format(time.process_time() - start_time))

main()
