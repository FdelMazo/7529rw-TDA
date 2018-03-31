def selectionSort(array):
	l = len(array)
	for i in range(l, 0, -1):
		m = array.index(obtenerMaxHasta(array, i))
		array[m], array[i - 1] = array[i - 1], array[m]
def obtenerMaxHasta(array, finArray):
    max = array[0]
    for i in range(finArray):
        if array[i] > max: max = array[i]
    return max