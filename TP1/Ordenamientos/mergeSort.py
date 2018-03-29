def mergeSort(array):
	if len(array)<2: return array
	medio = len(array)//2
	mitad1, mitad2 = array[:medio], array[medio:]
	izq = mergeSort(mitad1)
	der = mergeSort(mitad2)
	return _mergeSort(izq, der)

def _mergeSort(izq, der):
	resultado = []
	i, j = 0,0
	while i<len(izq) and j<len(der):
		if izq[i]<der[j]:
			resultado.append(izq[i])
			i+=1
		else:
			resultado.append(der[j])
			j+=1
	resultado.extend(izq[i:])
	resultado.extend(der[j:])
	return resultado