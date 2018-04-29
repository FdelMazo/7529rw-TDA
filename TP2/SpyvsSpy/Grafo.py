class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def __contains__(self, vertice):
        return vertice in self.grafo

    def __getitem__(self, vertice):
        return self.grafo[vertice]
    
    def __str__(self):
        return str(self.grafo)

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
    
