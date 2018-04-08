def selectionSort(array):
    l = len(array)
    for i in range(l):
        min_pos = obtenerMinPosDesde(array, i, l)
        array[min_pos], array[i] = array[i], array[min_pos]

def obtenerMinPosDesde(array, inicioArray, tam):
    min_pos = inicioArray
    for i in range(inicioArray,tam):
        if array[i] < array[min_pos]: min_pos = i
    return min_pos
