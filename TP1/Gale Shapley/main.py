from matchingGS import matchingGS
ARCHIVO  = "asignacion.txt"

def testMatchingGS():
    '''Prueba que ningun jugador este discontento con su equipo y que ese equipo lo hubiese preferido'''
    jugadores, equipos = matchingGS(200, 20, 10, ARCHIVO, True)
    for equipo in equipos.values():
        for jugador in equipo.getJugadores():
            descartados = jugador.getEquiposDescartados()
            for equipo_descartado in descartados:
                assert(equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador.getNumero()))
    print("El matching es estable: OK")

def main():
    matchingGS(200, 20, 10, ARCHIVO, False) #Cambiar a True si se quieren usar sets aleatorios

main()
testMatchingGS()
