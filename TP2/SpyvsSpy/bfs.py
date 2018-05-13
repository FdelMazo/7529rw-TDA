from queue import Queue
import sys

def minimoCaminoSinPeso(grafo, origen, final):
    if origen not in grafo or final not in grafo:
        return []
    orden, nivel = bfs(grafo, origen, final)
    camino = []
    v = final
    if v not in orden: return []
    for i in range(orden[v] - 1, -1, -1):
        camino.append(v)
        for w in grafo.adyacentes(v):
            if w in nivel[i]:
                v = w
                break
    camino.append(origen)
    camino.reverse()
    return camino

def distanciaSinPeso(grafo, origen, final):
    if origen not in grafo or final not in grafo:
        return -1
    orden, _ = bfs(grafo, origen, final)
    return orden[final] if final in orden else 0

def bfs(grafo, origen, final):
    visitados, orden, nivel = {}, {}, {}
    visitados[origen] = True
    nivel[0] = origen
    orden[origen] = 0
    _bfs(grafo, origen, final, visitados, orden, nivel)
    return orden, nivel

def _bfs(grafo, origen, final, visitados, orden, nivel):
    q = Queue()
    q.put(origen)
    while not q.empty():
        v = q.get()
        if v == final:
            break
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados[w] = True
                nivel[orden[v] + 1] = nivel.get(orden[v] + 1, []) + [w]
                orden[w] = orden[v] + 1
                q.put(w)