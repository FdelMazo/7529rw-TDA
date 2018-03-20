import random

def generarArrayRandom(n, low, high):
    return [int(n*random.random()) for i in xrange(low, high)]