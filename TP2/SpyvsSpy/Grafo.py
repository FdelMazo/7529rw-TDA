import math

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def __contains__(self, vertice):
        return vertice in self.grafo

    def __getitem__(self, vertice):
        return self.grafo[vertice]
    
    def adyacentes(self, vertice):
        return list(self.grafo[vertice].keys())
    
    def add(self, elemento):
        self.grafo[elemento] = {}
    
    def agregarArista(self, vertice1, vertice2):
        peso = 1
        if vertice1 not in self: self.add(vertice1)
        if vertice2 not in self: self.add(vertice2)
        self.grafo[vertice1][vertice2] = peso
        self.grafo[vertice2][vertice1] = peso

class GrafoPesado(Grafo):    
    def agregarArista(self, vertice1, vertice2):
        peso = self.calcularDistancia(vertice1, vertice2)
        if vertice1 not in self: self.add(vertice1)
        if vertice2 not in self: self.add(vertice2)
        self.grafo[vertice1][vertice2] = peso
        self.grafo[vertice2][vertice1] = peso
    
    def calcularDistancia(self, elemento1, elemento2):
        # El peso de la arista equivale a la distancia ecleudiana entre los dos vertices
        x1, y1 = elemento1
        x2, y2 = elemento2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    def distancia(self, vertice1, vertice2):
        return self[vertice1][vertice2]
