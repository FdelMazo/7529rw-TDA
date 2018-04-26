import math

class Grafo:
    def __init__(self):
        self.grafo = {}

    def existeVertice(self):
        return vertice in self.grafo.keys()

    def agregarVertice(self, elemento):
        self.grafo[elemento] = {}

    def agregarArista(self, elemento1, elemento2):
        distancia = self.calcularDistancia(elemento1, elemento2)
        self.grafo[elemento1][elemento2] = distancia
        self.grafo[elemento1][elemento2] = distancia

    def getAdyacentes(self, elemento):
        return self.grafo[elemento]

    def calcularDistancia(self, elemento1, elemento2):
        x1, y1 = elemento1
        x2, y2 = elemento2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
