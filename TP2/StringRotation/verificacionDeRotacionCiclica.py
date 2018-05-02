def rotarCadenaEnFormaHoraria(unaCadena):
	'''Recibe una cadena y la "rota en forma horaria", es decir, 
	pone su primer caracter al final.'''
	
	return (unaCadena[ 1: ( len( unaCadena ) ) ] + unaCadena[ 0 ] )

	''' 
	1 del return
	1 del + (En este caso el + es sintactic sugar de extend, pero k=1)
	unaCadena[ 1: ( len( unaCadena ) ) ] es O(n-1), ya que genera una
	nueva cadena de esa longitud.
	TOTAL = n - 1 + 1 + 1 = n + 1
	'''


def esRotacionCiclica(unaCadena, otraCadena, funcionDeRotacion):
	'''Recibe dos cadenas de igual tamaño y una funcion de rotación.
	Devuelve true si ambas son rotación cíclica con la función 
	especificada.'''
	unaCadenaAuxiliar = unaCadena
	longitudDeUnaCadena = len( unaCadena )
	
	for i in range( longitudDeUnaCadena ):
		unaCadenaAuxiliar = funcionDeRotacion( unaCadenaAuxiliar )
		
		if( unaCadenaAuxiliar == otraCadena ):
			return True

	return False

	''' 
	1 (asignar una variables) +
	2 (asignar una variable y hallar len) +
	1 (sentencia del for. ) +
	n (
		[ f(funcionDeRotacion) = n+1 ]  + 
		1 de asignar una variable
	 ) (n: longitud de las palabras
	1 del return 

	TOTAL = 1 + 2 + 1 + n( n+1 + 1) + 1 = n^2 + 2n + 5
	
	(en el peor caso, nunca se devuelve True)
	'''

def hayRotacionCiclica(unaCadena, otraCadena):
	'''Recibe dos cadenas de igual tamaño y devuelve true  si una 
	es una rotacion ciclica de la otra.'''		
	return (esRotacionCiclica(unaCadena, otraCadena, rotarCadenaEnFormaHoraria) or
	esRotacionCiclica(unaCadena[ : : -1 ], otraCadena, rotarCadenaEnFormaHoraria) )
	
	''' 1 por el return + 
		1 por el "or" + 
		[ f(esRotacionCiclica) = n^2 + 2n + 5] +
		n + [f(esRotacionCiclica)  n^2 + 2n + 5]
		(Invertir un arreglo se considera O(n) con n el tamaño del arreglo)
		
		TOTAL = 1 + 1 + n^2 + 2n + 5 + n + n^2 + 2n + 5
		= 12 + 4n + n^2
	'''
	
