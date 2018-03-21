from heapq import heapify, heappop

def heapSort(array):
        heapify(array)
        aux_heap = list(array)
        array.clear()
        while aux_heap:
            array.append(heappop(aux_heap))