import random

def generarSet(nombre, cantidad):
    arreglo =  random.sample(range(1,1000000), cantidad)
    file = open(nombre + ".txt","w")
    for i in range(cantidad):
            file.write(str(arreglo[i]) + "\n")
    file.close()

#generarSet("set1",10000)
