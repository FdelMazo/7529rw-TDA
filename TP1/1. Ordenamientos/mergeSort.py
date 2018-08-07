def mergeSort(array):
        l = len(array)
        if l < 2: return array
        izq, der = mergeSort(array[:l//2]), mergeSort(array[l//2:])
        resultado = []
        i, j = 0, 0
        while i < len(izq) and j < len(der):
                if izq[i] < der[j]:
                        resultado.append(izq[i])
                        i+=1
                else:
                        resultado.append(der[j])
                        j+=1
        resultado.extend(izq[i:]) if j == len(der) else resultado.extend(der[j:])
        return resultado
