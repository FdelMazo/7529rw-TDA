import random

def generarArrayRandom(n, low, high):
    return [int(n*random.random()) for i in range(low, high)]