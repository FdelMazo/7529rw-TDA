def insertionSort(array):
	l = len(array)
	for i in range(l):
            if i == (l - 1): return
            if array[i + 1] < array[i]:
                act = i + 1
                for j in range(i, -1, -1):
                    if array[act] < array[j]:
                        array[act], array[j], act = array[j], array[act], j
                    else: break