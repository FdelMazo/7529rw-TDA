def selectionSort(array):
	tamanio = len(array) - 1
	while tamanio > 0:
		pos_max = buscarMax(array, 0, tamanio)
		array[pos_max], array[tamanio] = array[tamanio], array[pos_max]
		tamanio -= 1


def buscarMax(array, inicio, fin):
	maxPos = inicio
	for i in range(inicio + 1, fin + 1, 1):
		if array[i] > array[maxPos]:
			maxPos = i
	return maxPos
