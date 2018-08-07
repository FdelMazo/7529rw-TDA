def KMP_matching(cadena, patron):
	'''
	Recibe dos cadenas no vacías, una de ellas es un patrón a buscar
	de la segunda (de menos caracteres). Devuelve True si el patrón 
	se encontraba en la cadena
	
	Implementáción de decisión en base a la versión en pseudocódigo del
	algoritmo que figura en: 
	"Introduction to Algorithms - Second Edition",  
	T.H. Cormen, C.E. Leiserson, R.L. Rivest y C. Stein.
	Página 926 (capítulo 32).
	'''
	n = len(cadena)
	m = len(patron)
	funcionDePrefijos = calcularFuncionDePrefijos(patron)
	numCoincidencias = 0
	
	for i in range(n):
		while (numCoincidencias > 0) and (patron[numCoincidencias] != cadena[i]):
			numCoincidencias = funcionDePrefijos[numCoincidencias - 1]
		
		if (patron[numCoincidencias] == cadena [i]):
			numCoincidencias +=  1
	
		if (numCoincidencias == m):
			return True
	
	return False


def calcularFuncionDePrefijos(patron):
	'''
	Función auxiliar de KMP_matching, utilizada para devolver
	la función (lista) de los prefijos del patrón.
	'''
	m = len(patron)
	funcionDePrefijos = []
	funcionDePrefijos.insert(0, 0)
	k = 0
	
	for q in range(1, m):
		while (k > 0) and (patron[k] != patron[q]):
			k = funcionDePrefijos[k - 1]
		
		if (patron[k] == patron[q]):
			k += 1
			
		funcionDePrefijos.insert(q,k)

	return funcionDePrefijos
