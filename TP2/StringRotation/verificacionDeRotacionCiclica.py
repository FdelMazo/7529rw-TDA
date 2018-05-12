def rotarCadenaEnFormaHoraria(unaCadena):
	'''Recibe una cadena y la "rota en forma horaria", es decir, 
	pone su primer caracter al final.'''
	
	return (unaCadena[ 1: ( len( unaCadena ) ) ] + unaCadena[ 0 ] )

	''' 
	1 del return
	1 del + (En este caso el + es syntactic sugar de extend, pero k=1)
	unaCadena[ 1: ( len( unaCadena ) ) ]: n-1, ya que genera una
	nueva cadena de esa longitud.
	1 del  unaCadena[ 0 ]
	TOTAL : 1 + 1 + n - 1 + 1 = n + 2
	'''


def esRotacionCiclica(unaCadena, otraCadena, funcionDeRotacion):
	'''Recibe dos cadenas de igual tamaño y una funcion de rotación.
	Devuelve true si ambas son rotación cíclica con la función 
	especificada.'''
	
	if ( len(unaCadena) != len(otraCadena) ): return False	
	unaCadenaAuxiliar = unaCadena
	longitudDeUnaCadena = len( unaCadena )
	
	for i in range( longitudDeUnaCadena ):
		unaCadenaAuxiliar = funcionDeRotacion( unaCadenaAuxiliar )
		
		if( unaCadenaAuxiliar == otraCadena ):
			return True

	return False

	''' 
	1 comparacion del if
	2 calcular len de dos cadenas
	(en el mejor caso el return false no se ejecuta)
	
	1 (asignar una variable) +
	2 (asignar una variable y hallar len) +
	1 (sentencia del for. ) +
	n (
		[ f(funcionDeRotacion) = n + 2 ]  + 
		1 de asignar una variable
		n de comparar dos cadenas de la misma cantidad de caracteres
	 ) (n: longitud de las palabras)
	1 del return 

	TOTAL = 1 + 2 + 1 + 2 + 1 + n( n + 2 + 1 + n) + 1 = 2n^2 + 3n + 8
	
	(en el peor caso, nunca se devuelve True)
	'''

def hayRotacionCiclica(unaCadena, otraCadena):
	'''Recibe dos cadenas de igual tamaño y devuelve true  si una 
	es una rotacion ciclica de la otra.'''	
	return esRotacionCiclica(unaCadena, otraCadena, rotarCadenaEnFormaHoraria)
	
	''' 1 por el return + 
		[ f(esRotacionCiclica) = 2n^2 + 3n + 8] 
		
		TOTAL = 1 + n^2 + 2n + 5 = 2n^2 + 3n + 9
	'''
	
