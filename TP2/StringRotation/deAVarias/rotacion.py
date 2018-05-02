def rotar_cadena(cadena, veces = 1):
	'''Recibe una cadena por parametro y la cantidad de veces que se la rotara. Devuelve una nueva cadena rotada veces cantidad de veces.'''
	
	return cadena[-veces:] + cadena[:-veces]


def es_rotacion_ciclica(cadena1, cadena2):
	'''Recibe dos cadenas pro parametro y devuelve si la segunda es una rotacion ciclica de la primera.'''
	
	for x in range(len(cadena1)):
		if rotar_cadena(cadena2, x) == cadena1:
			return True
	return False
