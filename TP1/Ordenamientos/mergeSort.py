def mergeSort(array):
        l = len(array)
        if l < 2: return array
        izq, der = mergeSort(array[:l//2]), mergeSort(array[l//2:])
        resultado = []
        cont_izq = 0
        cont_der = 0
        while cont_izq < len(izq) and cont_der < len(der):
                if izq[cont_izq] < der[cont_der]: 
                        resultado.append(izq[cont_izq])
                        cont_izq+=1
                else: 
                        resultado.append(der[cont_der])
                        cont_der+=1
        resultado.extend(izq[cont_izq:]) if cont_der == len(der) else resultado.extend(der[cont_der:])
        return resultado
