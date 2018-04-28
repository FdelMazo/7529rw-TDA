from heapq import *

def minimoCaminoConPeso(grafo, origen, final):
    padre = dijkstra(grafo, origen, final)
    camino = []
    v = final
    while v != None:
        camino.append(v)
        v = padre[v]
    return camino[::-1]

def dijkstra(grafo, origen, final):
    visitados = {}
    padre = {}
    distancia = {}
    if grafo.existeVertice(origen) and grafo.existeVertice(final):
        return _dijkstra(grafo, origen, visitados, padre, distancia)

def _dijkstra(grafo, origen, visitados, padre, distancia):
    heap = []
    v = origen
    heappush(heap, (0, v))
    while len(heap) > 0 :
        peso, (v) = heappop(heap)
        if v not in visitados:
            visitados[v] = True
            adyacentes = grafo.getAdyacentes(v)
            if v == origen:
                distancia[v] = 0
                padre[v] = None
            for w in adyacentes:
                if w not in distancia or distancia[w] > distancia[v] + adyacentes[w]:
                    distancia[w] = distancia[v] + adyacentes[w]
                    padre[w] = v
                heappush(heap, (float(distancia[w]), w))
    return padre