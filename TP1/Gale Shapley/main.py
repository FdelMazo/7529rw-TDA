from matchingGS import matchingGS

def testMatchingGS():
    '''Prueba que ningún jugador este discontento con su equipo y que ese equipo lo hubiese preferido'''
    jugadores, equipos = matchingGS(200, 20, 10, "asignacion.txt", False)
    for equipo in equipos.values():
        for jugador in equipo.getJugadores():
            descartados = jugador.getEquiposDescartados()
            for equipo_descartado in descartados:
                assert(equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador.getNumero()))
    print("OK")

def main():
    ''' Llamada a la función de asignación.
    '''
    matchingGS(200, 20, 10, "asignacion.txt", False) #Cambiar a True si se quieren usar nuevos sets aleatorios

main()
#testMatchingGS()