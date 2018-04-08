import random

def antiMerge(arreglo):
    if len(arreglo) < 2: return arreglo
    izq, der = [], []
    for x in arreglo[::2]: izq.append(x)
    for x in arreglo[1::2]: der.append(x)
    return antiMerge(izq) + antiMerge(der)

def generarSetAntiMerge(nombre, cantidad):
        arreglo = antiMerge(sorted(random.sample(range(cantidad), cantidad))[::-1])
        with open(nombre, "w") as archivo:
                for numero in arreglo:
                        archivo.write(str(numero) + "\n")

def generarSetDescendente(nombre, cantidad):
    archivo = open(nombre,"w")
    for i in range(cantidad, 0, -1):
        archivo.write(str(i) + "\n")
    archivo.close()

def generarRandomSet(nombre, cotaInf, cotaSup, cantidad):
    arreglo =  random.sample(range(cotaInf,cotaSup), cantidad)
    archivo = open(nombre,"w")
    for i in range(cantidad):
        archivo.write(str(arreglo[i]) + "\n")
    archivo.close()

generarRandomSet("SetRandom01.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom02.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom03.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom04.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom05.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom06.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom07.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom08.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom09.txt", 1, 1000000, 10000)
generarRandomSet("SetRandom10.txt", 1, 1000000, 10000)
generarSetAntiMerge("SetPeorCasoMergesort.txt", 10000)
generarSetDescendente("SetPeorCasoDescendente.txt", 10000)
