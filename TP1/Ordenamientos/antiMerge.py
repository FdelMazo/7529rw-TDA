def antiMerge(arreglo):
    '''Recibe un arreglo ordenado de mayor a menor y devuelve un arreglo nuevo como peor caso del algoritmo de ordenamientos de MergeSort'''
    if len(arreglo) < 2:
        return arreglo
    izq = []
    der = []
    for x in arreglo[::2]:
        izq.append(x)
    for x in arreglo[1::2]:
        der.append(x)
    return antiMerge(izq) + antiMerge(der)
