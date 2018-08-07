from minHeap import heapify, heappop

def heapSort(array):
    heapify(array, len(array))
    aux_heap = list(array)
    array.clear()
    while aux_heap:
        array.append(heappop(aux_heap))