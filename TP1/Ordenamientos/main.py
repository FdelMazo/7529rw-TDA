import argparse
import time
import os

from heapSort import heapSort
from mergeSort import mergeSort
from quickSort import quickSort
from insertionSort import insertionSort
from selectionSort import selectionSort

SORTS = [(mergeSort, "mergeSort"), (quickSort, "quickSort"), (heapSort, "heapSort")]
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
	print(lista_rutas)
	return lista_rutas

def rutaASet(ruta):
	'''Recibe una ruta de un archivo set y devuelve la cadena que representa a dicho set (ULTRA HARDCOREADO, hay que cambiarlo pero quiero visualizar el csv'''
	aux = ""
	for caracter in ruta:
		if caracter.isdigit():
			aux+=caracter
	return "set " + aux

def rutasASet(rutas):
	aux = ""
	for ruta in rutas:
		aux+= ','
		aux+= rutaASet(ruta)
	return aux[1:]

def exportCSV(diccionario, rutas):
	keys = sorted(diccionario.keys())
	cadena_aux = rutasASet(rutas)
	with open(os.path.join('.',"estadisticas.csv"), "w") as archivo:
		for key in keys:
			archivo.write(str(key) + " Elementos," + cadena_aux + "\n")
			aux = diccionario[key]
			setsKeys = sorted(aux.keys())
			for sort in sorted(aux[setsKeys[0]].keys()):
				linea = sort + ","
				for sets in setsKeys:
					linea+= str(aux[sets][sort])
					linea+= ","
				archivo.write(linea[:-1] + "\n")
			archivo.write("\n")
### ultra hardcore todo esto, despues lo hago ver mas lindo (juani) ###				

def main():
	'''	parser = argparse.ArgumentParser()
	parser.add_argument('set',help='Nombre de archivo de set', nargs='?', action = 'store', default = "sets/set1.txt")
	args = parser.parse_args()
	'''
	lista_rutas = sorted(rutasPorPalabra("set"))
	diccionario_auxiliar = {}
	for ruta_set in lista_rutas: # esto tiene que ser una funcion aparte, posiblemente dos
		for elementos in CANTIDAD_ELEMENTOS:
			diccionario_auxiliar[elementos] = diccionario_auxiliar.get(elementos, {})
			nombreSet = rutaASet(ruta_set)
			diccionario_auxiliar[elementos][nombreSet] = diccionario_auxiliar[elementos].get(nombreSet, {})
			print("\n\nComenzando ordenamientos sobre {} elementos\n".format(elementos))
			for ordenamiento in SORTS:
				print("Ejecutando {} con {} elementos del set '{}'".format(ordenamiento[0].__name__, elementos, ruta_set))
				start_time = time.process_time()
				lista = setALista(ruta_set, elementos)
				ordenamiento[0](lista)
				tiempo = time.process_time() - start_time
				diccionario_auxiliar[elementos][nombreSet][ordenamiento[1]] = tiempo
				print("Tiempo final de ejecucion: {} segundos \n".format(tiempo))
	exportCSV(diccionario_auxiliar, lista_rutas)

main()
