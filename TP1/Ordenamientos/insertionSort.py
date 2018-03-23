def insertionSort(array):
	n = len(array) - 1
	for i in range(0, n):
		if array[i + 1] < array[i]:
			relocate(array, i + 1)

def relocate(array, p):
	v = array[p]
	i = p
	while i > 0 and v < array[i - 1]:
		array[i] = array[i - 1]
		i -= 1
	array[i] = v
