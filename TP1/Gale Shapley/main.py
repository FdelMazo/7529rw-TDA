from matchingGS import matchingGS
from matchingGS import cargaDeArchivos
from Jugador import Jugador
from Equipo import Equipo

def testMatchingGS():
    '''Prueba que ningún jugador este discontento con su equipo y que ese equipo lo hubiese preferido'''
    jugadores, equipos = cargaDeArchivos(200,20,10)
    matchingGS(jugadores, equipos, 200, "asignacion.txt")
    for equipo in equipos.values():
        for jugador in equipo.getJugadores():
            descartados = jugador.getEquiposDescartados()
            for equipo_descartado in descartados:
                assert(equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador.getNumero()))
    print("OK")

def testMatchingGS2():
    ''''''
    jugadores, equipos = cargaDeArchivos(200,20,10)
    matchingGS(jugadores, equipos, 200, "asignacion.txt")
    for equipo_original in equipos.values():
        for jugador_original in equipo_original.getJugadores():
            descartados = jugador_original.getEquiposDescartados()
            for equipo_descartado in descartados:
                for jugador_externo in equipos[equipo_descartado].getJugadores():
                    condicion1 = equipo_original.getPosicionFavoritoActual() <= equipo_original.getPreferencias().index(jugador_externo.getNumero())
                    condicion2 = equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador_original.getNumero())
                    assert(condicion1 or condicion2)
    print("OK")

def main():
    ''' Llamada a la función de asignación.
    '''
    jugadores, equipos = cargaDeArchivos(200,20,10)
    matchingGS(jugadores, equipos, 200, "asignacion.txt") #Cambiar a True si se quieren usar nuevos sets aleatorios

main()
testMatchingGS()
testMatchingGS2()