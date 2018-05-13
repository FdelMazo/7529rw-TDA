from KMP_matching import *


def hayRotacionCiclicaConKMP(unaCadena, otraCadena):
	'''Recibe dos cadenas de igual tamaño y devuelve true si ambas son 
	rotación cíclica.'''
	
	if ( len(unaCadena) != len(otraCadena) ): return False	
	limiteDePatron = 0
	longitudDeOtraCadena = len (otraCadena) 
	
	while( (limiteDePatron < longitudDeOtraCadena) and
	KMP_matching(unaCadena, otraCadena[ : limiteDePatron + 1 ]) ):
		limiteDePatron += 1
		
	if ( limiteDePatron == longitudDeOtraCadena):
		return True
	
	return KMP_matching(unaCadena, otraCadena[ limiteDePatron : longitudDeOtraCadena ])
	

	''' 
	1 comparacion del if
	2 calcular la longitud de dos cadenas
	(en el peor caso nunca se devuelve false)
	1 (asignar una variable) +
	2 (asignar una variable y hallar la longitud de un arreglo) +
	1 sentencia del while
	n
	(
		1 (la primera comparación del while)
		1 (and del while)
		n (complejidad de KMP_matching)
		1 de hacer una operación matemática
		1 sumar de 1 a una variable
	)
	En el peor caso, el while se itera la mayor cantidad de veces, es
	decir, n (la cantidad de dígitos de la cadena), lo cual se da cuando
	las cadenas son iguales.
	
	2n de comparar dos cadenas de cantidad de caracteres n
	1 return del if
	
	TOTAL: 1 + 2 + 1 + 2 + 1 + n(1 + 1 + n + 1 + 1) + 2n + 1 =
	n^2 + 6n + 8
	'''
	
