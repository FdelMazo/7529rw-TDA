def setALista(nombre_archivo):
	lista = []
	with open(nombre_archivo) as archivo:
		for linea  in archivo:
			lista.append(linea.strip())
	return lista

def actualizarDiccionarioResultados(resultados, set, elementos, sort, tiempo):
    resultados[elementos] = resultados.get(elementos, {})
    resultados[elementos][set] = resultados[elementos].get(set, {})
    resultados[elementos][set][sort] = tiempo

def exportCSV(resultados, sets):
	with open("Salida.csv", "w") as archivo:
		for cantidadElementos in sorted(resultados.keys()):
			archivo.write("{} Elementos,".format(str(cantidadElementos)) + ','.join(sets) + "\n")
			diccionarioAux = resultados[cantidadElementos]
			sets = sorted(diccionarioAux.keys())
			sorts = sorted(diccionarioAux[sets[0]].keys())
			for sort in sorts:
				linea = sort + ','
				for set in sets:
					linea+= str(diccionarioAux[set][sort]) + ','
				archivo.write(linea[:-1] + "\n")
			archivo.write("\n")
