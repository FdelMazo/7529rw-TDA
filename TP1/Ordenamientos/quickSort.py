def quickSort(array):
    if len(array) < 2 :
        return array
    array_menores, array_pivotes, array_mayores = _particion(array)
    return quickSort(array_menores) + array_pivotes + quickSort(array_mayores)

def _particion(array):
    pivot = array[0]
    menores = []
    pivotes = []
    mayores = []
    for elemento in array:
        if elemento < pivot:
            menores.append(elemento)
        elif elemento == pivot:
            pivotes.append(elemento)
        else:
            mayores.append(elemento)
    return menores, pivotes, mayores