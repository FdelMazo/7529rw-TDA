def heapify(array, cantidadElementos):
    '''
    '''
    for i in range(cantidadElementos//2, 0, -1):
        downheap(array, i - 1, cantidadElementos)


def downheap(heap, pos, cantidadElementos):
    '''
    '''
    posicionHijoIzquierdo = (pos * 2) + 1
    posicionHijoDerecho = (pos * 2) + 2
        
    if(posicionHijoIzquierdo >= cantidadElementos and posicionHijoDerecho >= cantidadElementos):
        return
        
    if posicionHijoIzquierdo >= cantidadElementos:
        posicionHijoMayor =  posicionHijoDerecho
    
    elif posicionHijoDerecho >= cantidadElementos:
        posicionHijoMayor =  posicionHijoIzquierdo
    
    elif heap[posicionHijoIzquierdo] < heap[posicionHijoDerecho]:
        posicionHijoMayor =  posicionHijoIzquierdo
    
    else:
        posicionHijoMayor = posicionHijoDerecho
        
    if (heap[pos] > heap[posicionHijoMayor]):
        heap[pos],  heap[posicionHijoMayor] = heap[posicionHijoMayor],  heap[pos]
        downheap(heap, posicionHijoMayor, cantidadElementos)
    
    
def upheap(heap, pos):
    '''
    '''
    auxPos = (pos - 1) // 2
    if(pos > 0 and (heap[pos] < heap[auxPos])):
        heap[pos],  heap[auxPos] = heap[auxPos],  heap[pos]
        pos = auxPos;
        upheap(heap, pos)
        
    
def heappush(heap, elemento):
    '''
    '''
    cantidadElementos = len(heap)
    heap[cantidadElementos] = elemento
    upheap(heap, cantidadElementos)
    
    
def heappop(heap):
    '''
    '''
    cantidadElementos = len(heap)
    if cantidadElementos==0:
        return None
    
    elemento = heap[0]
    heap[0] = heap[cantidadElementos - 1]
    downheap(heap, 0, cantidadElementos)
    heap.pop()
    return elemento