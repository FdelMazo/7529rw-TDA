from queue import Queue

def minimoCaminoSinPesos(grafo, origen, final):
    orden, nivel = bfs(grafo, origen, final)
    return bfsGetMinimoCamino(grafo, origen, final, orden, nivel)

def bfs(grafo, origen, final):
    visitados = {}
    orden = {}
    nivel = {}
    if grafo.existeVertice(origen):
        visitados[origen] = True
        nivel[0] = origen
        orden[origen] = 0
        bfsVisitar(grafo, origen, final, visitados, orden, nivel)
    return orden, nivel

def bfsVisitar(grafo, origen, final, visitados, orden, nivel):
    q = Queue()
    q.put(origen)
    while not q.empty():
        v = q.get()
        if v == final:
            break
        for w in grafo.getAdyacentes(v):
            if w not in visitados:
                visitados[w] = True
                nivel[orden[v] + 1] = nivel.get(orden[v] + 1, []) + [w]
                orden[w] = orden[v] + 1
                q.put(w)


def bfsGetMinimoCamino(grafo, origen, final, orden, nivel):
    camino = []
    ordenFinal = orden[final]
    v = final
    for i in range(ordenFinal - 1, -1, -1):
        camino.append(v)
        for w in grafo.getAdyacentes(v):
            if w in nivel[i]:
                v = w
                break
    camino.append(origen) #Odio tener que hacer esto, pero no encuentro otra manera
    return camino[::-1]