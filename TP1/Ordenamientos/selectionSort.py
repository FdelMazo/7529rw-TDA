def selectionSort(array):
    l = len(array)
    for i in range(l, 0, -1):
        max_pos = obtenerMaxPosHasta(array, i)
        array[max_pos], array[i - 1] = array[i - 1], array[max_pos]

def obtenerMaxPosHasta(array, finArray):
    max_pos = 0
    for i in range(finArray):
        if array[i] > array[max_pos]: max_pos = i
    return max_pos
