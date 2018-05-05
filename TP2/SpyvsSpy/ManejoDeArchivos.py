from Grafo import *
from GrafoPesado import *
from math import factorial
import random

def lineasToVertices(numeros_de_linea):
    vertices = []
    numeros_de_linea = sorted([int(x) for x in numeros_de_linea])
    with open('mapa.coords') as file:
        lineas_file = file.readlines()
        for linea in numeros_de_linea:
            vertice = lineas_file[linea].split('-')[0]
            vertice = vertice.strip()
            vertice = tuple([int(x) for x in vertice.split()])
            vertices.append(vertice)
    return vertices

def cantidad_lineas():
    with open('mapa.coords') as file:
        n = len(file.readlines())
    return n

def elegirTresLineasAlAzar():
    n = cantidad_lineas()
    return [random.randint(0,n-1) for x in range(3)]
    
def combinacionesPosibles(n, r):
    numerador = factorial(n)
    divisor = factorial(r) * factorial(n - r)
    return numerador/divisor

def generarArchivo(dimensionX, dimensionY, cantidadPuntos):
    """Crea el archivo 'mapa.coords' que es un grafo representado con una matriz de dimension dada
    donde las lineas especifican una conexion entre puntos de la ciudad"""
    n,r = dimensionX*dimensionY, 2
    if cantidadPuntos > combinacionesPosibles(n,r):
        cantidadPuntos = combinacionesPosibles(n,r)
    conexiones = set()
    while len(conexiones) < cantidadPuntos:
        punto1 = ( random.randint(0,dimensionX-1) , random.randint(0,dimensionY-1) )
        punto2 = ( random.randint(0,dimensionX-1) , random.randint(0,dimensionY-1) )
        if punto1 == punto2: continue
        tuplaordenada = (punto1,punto2) if punto1 < punto2 else (punto2,punto1)
        conexiones.add( tuplaordenada )
    conexiones = sorted(conexiones)
    with open('mapa.coords','w') as file:
        for p1,p2 in conexiones:
            linea = "{} {} - {} {}\n".format(*p1, *p2)
            file.write(linea)

def crearGrafoDesdeArchivo(archivo='mapa.coords', pesado=False):
    """Recibe un archivo de texto.
    El archivo de texto debe tener en cada linea las coordenadas en la formax1 y1 - x2 y2 representando
    la union de dos vertices.
    Devuelve un grafo"""
    grafo = GrafoPesado() if pesado else Grafo()
    with open(archivo, "r") as archivo:
        for linea in archivo:
            v1,v2 = stringADosVertices(linea)
            grafo.add(v1)
            grafo.add(v2)
            grafo.agregarArista(v1, v2)
    return grafo

def stringADosVertices(linea):
    datos = linea.split()
    datos.pop(2) #Sacar el guion
    datos = [int (x) for x in datos]
    x1,y1,x2,y2 = datos
    return ( (x1, y1) , (x2,y2) )


if __name__ == '__main__':
	generarArchivo(10,10,0.7*10*10)
	print(crearGrafoDesdeArchivo('mapa.coords'))