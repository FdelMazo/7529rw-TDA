def quickSort(array):
    if len(array) < 2 : return array
    pivote = array[0]
    menores, mayores = [], []
    for x in range(1, len(array)):
        if array[x] < pivote:
            menores.append(array[x])
        else:
            mayores.append(array[x])         
    return quickSort(menores) + [pivote] + quickSort(mayores)