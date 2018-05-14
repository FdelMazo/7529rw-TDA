from KMP_matching import KMP_matching

def hayRotacionCiclicaMejorada(unaCadena, otraCadena,):
	'''Recibe dos cadenas y devuelve true si ambas son rotación
	 cíclica.'''
	if ( len(unaCadena) != len(otraCadena) ): return False	
	return KMP_matching(otraCadena + otraCadena,  unaCadena)

	''' 
	2 de calcular la longitud de dos cadenas
	1 de la comparación entre longitudes
	2n de generar una cadena con dos veces la longitud de la original
	2n + n de la complejidad del algoritmo de KMP
	TOTAL = 5n + 3
	(en el peor caso, no se devuelve False).
	'''
