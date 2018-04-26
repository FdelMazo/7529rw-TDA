from grafo import *

def crearGrafo(archivo):
    """Recibe un archivo de texto.
    El archivo de texto debe tener en cada linea las coordenadas en la forma x1 y1 - x2 y2 representando
    la union de dos vertices.
    Devuelve un grafo"""
    grafo = Grafo()
    with open(archivo, "r") as archivo:
        for linea in archivo:
            datos = linea.split(" ")
            vertice1 = listaDePalabrasAVertice(datos[:2])
            vertice2 = listaDePalabrasAVertice(datos[3::])
            grafo.agregarVertice(vertice1)
            grafo.agregarVertice(vertice2)
            grafo.agregarArista(vertice1, vertice2)
    return grafo

def listaDePalabrasAVertice(lista):
    x = int(lista[0])
    y = int(lista[1])
    return (x, y)