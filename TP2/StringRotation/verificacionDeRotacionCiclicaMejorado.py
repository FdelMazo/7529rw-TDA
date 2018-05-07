
def esRotacionCiclicaMejorada(unaCadena, otraCadena,):
	'''Recibe dos cadenas y devuelve true si ambas son rotación
	 cíclica.'''
	if ( len(unaCadena) != len(otraCadena) ): return False	
	return KMP_matching(otraCadena + otraCadena,  unaCadena)

	''' 
	2 de calcular la longitud de dos cadenas
	1 de la comparación entre longitudes
	1 del return
	2n de generar una cadena con dos veces la longitud de la original
	n de la complejidad del algoritmo de KMP
	O(3n + 3)
	(en el peor caso, el False no se ejecuta).
	'''
