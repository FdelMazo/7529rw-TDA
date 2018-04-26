from queue import Queue

def bfs(grafo, origen, final):
    visitados = {}
    orden = {}
    nivel = {}
    if grafo.existeVertice(origen):
        visitados[origen] = True
        nivel[0] = origen
        orden[origen] = 0
        bfsVisitar(grafo, origen, final, visitados, orden, nivel)


def bfsVisitar(grafo, origen, final, visitados, orden, nivel):
    q = Queue()
    q.put(origen)
    while not q.empty():
        v = q.get()
        if v == final:
            break
        for w in grafo.getAdyacentes(v):
            visitados[w] = True
            nivel[orden[v] + 1] = nivel.get(orden[v] + 1, []) + [w]
            orden[w] = orden[v] + 1
            q.put(w)

