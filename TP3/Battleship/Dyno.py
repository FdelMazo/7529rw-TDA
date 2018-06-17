from Jugador import Jugador
from copy import deepcopy
from copy import copy
from heapq import heappush, heappop
import itertools

import itertools
def allSubsetsMoreThan(lista, objetivo):
	combs = []
	for i in range(len(lista)):
		for c in itertools.combinations(lista, i):
			if sum(c) >= objetivo:
				combs.append(list(c))
	return combs

def removeDups(combs):
	newCombs = []
	for c in combs:
		if c in newCombs: continue
		newCombs.append(c)
	return newCombs

def sacarSobrantes(comb, ts):
	for elem in comb[:]:
		indice = comb.index(elem)
		comb.remove(elem)
		if sum(comb) >= ts:
			continue
		comb.insert(indice, elem)

def listaAIndices(lista, listaOriginal):
	listaIndices = []
	for elem in lista:
		indice = listaOriginal.index(elem)
		while indice in listaIndices:
			indice += listaOriginal[indice+1:].index(elem) +1
		listaIndices.append(indice)
	return listaIndices

def combinacionesMatadoras(objetivo, listaOriginal):
	resultados = []
	combinaciones = allSubsetsMoreThan(listaOriginal, objetivo)
	for combinacion in combinaciones:
		sacarSobrantes(combinacion, objetivo)
	combinaciones = removeDups(combinaciones)
	for combinacion in combinaciones:
		indexes = listaAIndices(combinacion, listaOriginal)
		resultados.append(indexes)
	return resultados

def combinacionesParaBarco(fila, barco, cantidadLanzaderas):
	combinaciones = combinacionesMatadoras(barco.getVida(), fila)
	combinacionesMatadorasBarco = []
	for combinacion in combinaciones:
		for i, turnos in enumerate(combinacion):
			turnos = [turnos] + [None] * (cantidadLanzaderas - 1)
			combinacion[i] = turnos
		if combinacion not in combinacionesMatadorasBarco: combinacionesMatadorasBarco.append(combinacion)
	return combinacionesMatadorasBarco

def encontrarTodaCombinacionParaTodoBarco(matriz, barcos, cantidadLanzaderas):
	turnosParaTodos = {}
	for y,fila in enumerate(matriz):
		turnosDondeMuere = combinacionesParaBarco(fila, barcos[y], cantidadLanzaderas)
		if turnosDondeMuere: turnosParaTodos[barcos[y]] = sorted(turnosDondeMuere)
	return turnosParaTodos

def ordenarPorBarcoMasDificilDeMatar(turnosParaTodos):
	heapBarcosDificiles = []
	for barco in turnosParaTodos:
		cantPosiblesCombinaciones = len(turnosParaTodos[barco])
		heappush(heapBarcosDificiles, (cantPosiblesCombinaciones, barco.getID()))
	return heapBarcosDificiles

def simularPartidaConPartidaParcial(partidaParcial, partidaBarcoActual, cantidadLanzaderas):
	for turnoParcial, turnoActual in zip(partidaParcial, partidaBarcoActual):
		if turnoActual and turnoParcial and all([x for x in turnoParcial if x!=0]): return False
	partidaResultado = []
	for turnoParcial, turnoActual in zip(partidaParcial, partidaBarcoActual):
		turnoParcialValido = [x for x in turnoParcial if x!=None] if turnoParcial else []
		turnoActualValido = [x for x in turnoActual if x!=None] if turnoActual else []
		if len(turnoParcialValido) + len(turnoActualValido) <= cantidadLanzaderas:
			turnoNuevo = turnoParcialValido + turnoActualValido
			partidaResultado.append(turnoNuevo+[None]*(cantidadLanzaderas-len(turnoNuevo)))
	partidaResultado += partidaParcial[len(partidaResultado):]
	partidaResultado += partidaBarcoActual[len(partidaResultado):]
	return partidaResultado

def definirPartidaAJugar(heapDeBarcosDificiles, turnosParaTodos, partidasPorBarco, barcos, cantidadLanzaderas):
    resultados = partidasPorBarco
    while heapDeBarcosDificiles:
        _, barcoActualID = heappop(heapDeBarcosDificiles)
        partidasBarcoActual = combinacionDePosibilidadesAPartidas(barcoActualID,
                                                              turnosParaTodos[barcos[barcoActualID]])
        for i, partida in enumerate(resultados):
            partidasPosiblesAAppendear = []
            for partidaActual in partidasBarcoActual:
                partidaPosible = simularPartidaConPartidaParcial(partida, partidaActual, cantidadLanzaderas)
                if partidaPosible and partidaPosible not in partidasPosiblesAAppendear: partidasPosiblesAAppendear.append(
                    partidaPosible)
            if partidasPosiblesAAppendear: resultados[i] = minimosPuntos(partidasPosiblesAAppendear)
    return resultados

def jugarPrimeraPartida(resultados, barcos):
    primeraPartida = minimosPuntos(resultados)
    barcosRemanentes = None
    barcosDePrimeraPartida = []
    for sublist in primeraPartida:
        if not sublist: continue
        for item in sublist:
            if item != None and item not in barcosDePrimeraPartida:
                barcosDePrimeraPartida.append(item)
    if barcosDePrimeraPartida:
        barcosRemanentes = [b for b in barcos if b.getID() not in barcosDePrimeraPartida]
    else:
        barcosRemanentes = [b for b in barcos if b.getID()]
    return primeraPartida, barcosRemanentes

def jugarSegundaPartida(barcosRemanentes, primeraPartida, matriz, cantidadLanzaderas):
    segundaPartida = []
    for b in barcosRemanentes:
        vida = b.getVida()
        id = b.getID()
        for i, turno in enumerate(primeraPartida):
            turnoNuevo = copy(turno)
            if turno and all([x for x in turno if x != 0]):
                pass
            elif not turno:
                turnoNuevo = [b.getID()] * (cantidadLanzaderas)
                vida -= cantidadLanzaderas * matriz[id][i - 1]
            else:
                for i, lanzadera in enumerate(turno):
                    if lanzadera == None:
                        turnoNuevo[i] = b.getID()
                        vida -= matriz[id][i - 1]
            segundaPartida.append(turnoNuevo)
        while (vida > 0):
            segundaPartida.append([b.getID()] * (cantidadLanzaderas))
            vida -= cantidadLanzaderas * matriz[id][i - 1]
        segundaPartida.append([b.getID()] * (cantidadLanzaderas))
    return segundaPartida


class Dyno(Jugador):
	"""
	Dyno:
		Juega partidas reducidas, y en base a esas genera nuevas partidas. Así, hasta llegar a la mejor partida.

		La reduccion consiste en partidas de una lanzadera y un barco

		Entonces, iterando desde barco mas dificil de matar:
			- Busca cuales son sus partidas posibles a jugar
			- De lo que ya tenia memorizado, busca las partidas posibles para jugar con un barco mas que lo anterior
			- De las combinaciones, elige la mejor partida
	"""

	def __init__(self):
		super().__init__('Dyno')

	def elegirTargetsDeLaPartida(self, partidaOriginal):
		matriz, barcos, cantidadLanzaderas = partidaOriginal.getMatriz(), partidaOriginal.getBarcosVivos(), partidaOriginal.getCantidadLanzaderas()

		turnosParaTodos = encontrarTodaCombinacionParaTodoBarco(matriz, barcos, cantidadLanzaderas)
		heapDeBarcosDificiles = ordenarPorBarcoMasDificilDeMatar(turnosParaTodos)
		_, barcoActualID = heappop(heapDeBarcosDificiles)
		partidasPorBarco = combinacionDePosibilidadesAPartidas(barcoActualID, turnosParaTodos[barcos[barcoActualID]])

		resultados = definirPartidaAJugar(heapDeBarcosDificiles, turnosParaTodos, partidasPorBarco, barcos, cantidadLanzaderas)

		primeraPartida, barcosRemanentes = jugarPrimeraPartida(resultados, barcos)
		if not barcosRemanentes: return primeraPartida

		segundaPartida = jugarSegundaPartida(barcosRemanentes, primeraPartida, matriz, cantidadLanzaderas)
		return segundaPartida

def contadoresPeorTurno(partida):
	lanzaderas = 0
	for turno in partida:
		if turno:
			lanzaderas=len(turno)
			break
	contadorNones = 0
	for turno in partida:
		if turno: contadorNones += turno.count(None)
		else: contadorNones += lanzaderas
	return contadorNones

def minimosPuntos(partidas):
	atributoPartidas = []
	for partida in partidas:
		atributoPartidas.append((partida,contadoresPeorTurno(partida)))
	return max(atributoPartidas, key= lambda x: -x[1])[0]


def combinacionDePosibilidadesAPartidas(idBarco, posibilidades):
	partidas = []
	for posibilidad in posibilidades:
		partida = []
		for turno in posibilidad:
			while len(partida) <= turno[0]: partida += [None]
			partida[turno[0]] = [idBarco] + [None] * (len(turno)-1)
		partidas.append(partida)
	return partidas

if __name__=='__main__':
	from Juego import Juego
	from Partida import Partida

	archivo = 'grilla.coords'
	matriz = Juego.ArchivoToMatriz(archivo)
	barcos = Juego.ArchivoToBarcos(archivo)
	cantidadLanzaderas = 3

	juego = Juego(matriz, barcos, cantidadLanzaderas)
	jugador = Dyno()
	partida = Partida(matriz, barcos, cantidadLanzaderas, jugador)
	partida.setPosicionesIniciales()
	targets = jugador.elegirTargetsDeLaPartida(partida)

	print(targets)
