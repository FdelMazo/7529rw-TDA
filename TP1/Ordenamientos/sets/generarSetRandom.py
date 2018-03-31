import random

def generarSet(nombre, cotaInf, cotaSup, cantidad):
    arreglo =  random.sample(range(cotaInf,cotaSup), cantidad)
    archivo = open(nombre,"w")
    for i in range(cantidad):
            archivo.write(str(arreglo[i]) + "\n")
    archivo.close()

generarSet("set1.txt", 1, 1000000, 10000)
generarSet("set2.txt", 1, 1000000, 10000)
generarSet("set3.txt", 1, 1000000, 10000)
generarSet("set4.txt", 1, 1000000, 10000)
generarSet("set5.txt", 1, 1000000, 10000)
generarSet("set6.txt", 1, 1000000, 10000)
generarSet("set7.txt", 1, 1000000, 10000)
generarSet("set8.txt", 1, 1000000, 10000)
generarSet("set9.txt", 1, 1000000, 10000)
generarSet("set10.txt", 1, 1000000, 10000)