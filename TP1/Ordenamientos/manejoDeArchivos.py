import os

def setALista(nombre_archivo, cantidadElementos):
	lista = []
	with open(nombre_archivo) as archivo:
		for linea, i  in zip(archivo,range(cantidadElementos)):
			lista.append(linea.strip())
	return lista

def rutasPorPalabra(palabra):
	'''Recibe una palabra por parametro y devuelve las rutas (en una lista) de los archivos cuyo nombre contenga a dicha palabra '''
	lista_rutas = []
	for origen, carpetas, contenido in os.walk('.'):
		for archivo in contenido:
			if palabra in archivo:
				lista_rutas.append((os.path.join(origen, archivo)))
	print(lista_rutas)
	return lista_rutas

def rutaASet(ruta):
    '''Recibe una ruta de un archivo set y devuelve la cadena que representa a dicho set (ULTRA HARDCOREADO, hay que cambiarlo pero quiero visualizar el csv'''
    lista = ruta.split("/")
    nombre = lista[-1]
    return nombre[:-4]

def rutasASet(rutas):
	aux = ""
	for ruta in rutas:
		aux+= ','
		aux+= rutaASet(ruta)
	return aux[1:]

def exportCSV(diccionario, rutas, nombre):
    keys = sorted(diccionario.keys())
    cadena_aux = rutasASet(rutas)
    nombre = str(nombre) + ".csv"
    with open(os.path.join('.', nombre), "w") as archivo:
        for key in keys:
            archivo.write(str(key) + " Elementos," + cadena_aux + "\n")
            aux = diccionario[key]
            setsKeys = sorted(aux.keys())
            for sort in sorted(aux[setsKeys[0]].keys()):
                linea = sort + ","
                for sets in setsKeys:
                    linea+= str(aux[sets][sort])
                    linea+= ","
                archivo.write(linea[:-1] + "\n")
            archivo.write("\n")
### ultra hardcore todo esto, despues lo hago ver mas lindo (juani) ###