from heapq import *

def minimoCaminoConPeso(grafo, origen,final):
    if origen not in grafo or final not in grafo:
        return 0
    padre, distancia = dijkstra(grafo, origen)
    camino = []
    v = final
    if v not in padre: return []
    while v is not None:
        camino.append(v)
        v = padre[v]
    camino.reverse()
    return camino

def distanciaConPeso(grafo, origen, final):
    if origen not in grafo or final not in grafo:
        return -1
    _, distancia = dijkstra(grafo, origen)
    return distancia[final] if final in distancia else 0

def dijkstra(grafo, origen):
    visitados, padre, distancia = {}, {}, {}
    return _dijkstra(grafo, origen, visitados, padre, distancia)

def _dijkstra(grafo, origen, visitados, padre, distancia):
    heap = []
    distancia[origen] = 0
    padre[origen] = None
    heappush(heap, (distancia[origen], origen))
    while len(heap) > 0 :
        peso, v = heappop(heap)
        if v not in visitados:
            visitados[v] = True
            for w in grafo.adyacentes(v):
                if w not in distancia or distancia[w] > distancia[v] + grafo.distancia(v,w):
                    distancia[w] = distancia[v] + grafo.distancia(v,w)
                    padre[w] = v
                heappush(heap, (distancia[w], w))
    return padre,distancia