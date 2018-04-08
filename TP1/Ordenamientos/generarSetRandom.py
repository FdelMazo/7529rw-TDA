import random

def generarSet(nombre, cotaInf, cotaSup, cantidad):
    arreglo =  random.sample(range(cotaInf,cotaSup), cantidad)
    archivo = open(nombre,"w")
    for i in range(cantidad):
            archivo.write(str(arreglo[i]) + "\n")
    archivo.close()

generarSet("SetRandom01.txt", 1, 1000000, 10000)
generarSet("SetRandom02.txt", 1, 1000000, 10000)
generarSet("SetRandom03.txt", 1, 1000000, 10000)
generarSet("SetRandom04.txt", 1, 1000000, 10000)
generarSet("SetRandom05.txt", 1, 1000000, 10000)
generarSet("SetRandom06.txt", 1, 1000000, 10000)
generarSet("SetRandom07.txt", 1, 1000000, 10000)
generarSet("SetRandom08.txt", 1, 1000000, 10000)
generarSet("SetRandom09.txt", 1, 1000000, 10000)
generarSet("SetRandom10.txt", 1, 1000000, 10000)
