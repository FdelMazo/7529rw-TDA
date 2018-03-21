import random

def generarSet(nombre, cantidad):
    arreglo =  random.sample(range(1,1000000), cantidad)
    file = open(nombre + ".txt","w")
    for i in range(cantidad):
        file.write(str(arreglo[i]) + "\n")
    file.close() 

generarSet("set1",10000)
generarSet("set2",10000)
generarSet("set3",10000)
generarSet("set4",10000)
generarSet("set5",10000)
generarSet("set6",10000)
generarSet("set7",10000)
generarSet("set8",10000)
generarSet("set9",10000)
generarSet("set10",10000)