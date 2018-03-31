def quickSort(array):
    if len(array) < 2 : return array
    pivote = array[0]
    menores, pivotes, mayores = [], [], []
    for elemento in array:
        if elemento < pivote:
            menores.append(elemento)
        else:
            pivotes.append(elemento) if (elemento == pivote) else mayores.append(elemento)            
    return quickSort(menores) + pivotes + quickSort(mayores)