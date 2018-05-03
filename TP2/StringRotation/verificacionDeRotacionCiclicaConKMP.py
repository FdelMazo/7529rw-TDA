from KMP_matching import *


def hayRotacionCiclicaConKMP(unaCadena, otraCadena):
	'''Recibe dos cadenas de igual tamaño y devuelve true si ambas son 
	rotación cíclica.'''
	
	limiteDePatron = 0
	longitudDeOtraCadena = len (otraCadena) 
	
	while( (limiteDePatron < longitudDeOtraCadena) and
	KMP_matching(unaCadena, otraCadena[ : limiteDePatron + 1 ]) ):
		limiteDePatron += 1
		
	if ( limiteDePatron == longitudDeOtraCadena):
		return True
	
	return KMP_matching(unaCadena, otraCadena[ limiteDePatron : longitudDeOtraCadena ])
	

	''' 
	1 (asignar una variable) +
	2 (asignar una variable y hallar la longitud de un arreglo) +
	2 (asignar una variable y hallar la longitud de un arreglo) +
	1 (la primera comparación del while)
	1 (and del while)
	f(n) (complejidad de KMP_matching)
	n(
		1 (asignar una variable)
	)
	En el peor caso, el while se itera la mayor cantidad de veces, es
	decir, n (la cantidad de dígitos de la cadena), lo cual se da cuando
	las cadenas son iguales.
	
	1 comparación del if
	1 return if
	'''
	
