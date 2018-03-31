def mergeSort(array):
        l = len(array)
        if l < 2: return array
        izq, der = mergeSort(array[:l//2]), mergeSort(array[l//2:])
        resultado = []
        while izq and der:
                if izq[0] < der[0]: resultado.append(izq.pop(0))
                else: resultado.append(der.pop(0))
        resultado.extend(izq) if izq else resultado.extend(der)
        return resultado