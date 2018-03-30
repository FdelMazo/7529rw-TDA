def generarSetDescendente(nombre, cantidad):
    arreglo = []
    archivo = open(nombre + ".txt", "w")
    for i in range(cantidad, 0, -1):
        archivo.write(str(i) + "\n")
    archivo.close()

def generarSetAscendente(nombre, cantidad):
    arreglo = []
    archivo = open(nombre + ".txt", "w")
    for i in range(0, cantidad, 1):
        archivo.write(str(i) + "\n")
    archivo.close()

generarSetDescendente("descendente", 10000)
generarSetAscendente("ascendente", 10000)