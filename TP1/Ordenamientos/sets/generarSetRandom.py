import random

def generarSet(nombre, cantidad):
    arreglo =  random.sample(range(1,1000000), cantidad)
    archivo = open(nombre + ".txt","w")
    for i in range(cantidad):
            archivo.write(str(arreglo[i]) + "\n")
    archivo.close()

#generarSet("set1",10000)
