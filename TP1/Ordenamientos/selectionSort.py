def selectionSort(array):
	n = len(array) - 1
	while n > 0:
		p = findMax(array, 0, n)
		array[p], array[n] = array[n], array[p]
		n -= 1


def findMax(array, a, b):
	maxPos = a
	for i in range(a + 1, b + 1, 1):
		if array[i] > array[maxPos]:
			maxPos = i
	return maxPos
