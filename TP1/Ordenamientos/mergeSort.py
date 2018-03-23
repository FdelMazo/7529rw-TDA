def mergeSort(array):
	n = len(array) - 1
	while n > 0:
		p = findMax(array, 0, n)
		array[p], array[n] = array[n], array[p]
		n -= 1
