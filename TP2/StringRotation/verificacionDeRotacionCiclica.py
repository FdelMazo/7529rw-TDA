def rotarCadenaEnFormaHoraria(unaCadena):
	'''Recibe una cadena y la "rota en forma horaria", es decir, 
	pone su primer caracter al final.'''
	
	return (unaCadena[ 1: ( len( unaCadena ) ) ] + unaCadena[ 0 ] )


def esRotacionCiclica(unaCadena, otraCadena, funcionDeRotacion):
	'''Recibe dos cadenas de igual tamaño y una funcion de rotación.
	Devuelve true si ambas son rotación cíclica con la función 
	especificada.'''
	unaCadenaAuxiliar = unaCadena
	
	for i in range( len( unaCadena ) ):
		unaCadenaAuxiliar = funcionDeRotacion( unaCadenaAuxiliar )
		
		if( unaCadenaAuxiliar == otraCadena ):
			return True

	return False


def hayRotacionCiclica(unaCadena, otraCadena):
	'''Recibe dos cadenas de igual tamaño y devuelve true  si una 
	es una rotacion ciclica de la otra.'''		
	return (esRotacionCiclica(unaCadena, otraCadena, rotarCadenaEnFormaHoraria) or
	esRotacionCiclica(unaCadena[ : : -1 ], otraCadena, rotarCadenaEnFormaHoraria) )

