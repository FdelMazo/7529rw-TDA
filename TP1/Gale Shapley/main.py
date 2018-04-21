from matchingGS import matchingGS
from matchingGS import cargaDeArchivos
from Jugador import Jugador
from Equipo import Equipo

RUTA = "asignacion.txt"
EQUIPOS = 20
JUGADORES = 200
VACANTES = 10


def testPreferenciasGS():
    '''Prueba que dadas las asignaciones finales, ningún jugador este discontento con su equipo y que ninguno de sus equipos favoritos lo hubiese preferido'''
    jugadores, equipos = cargaDeArchivos(JUGADORES,EQUIPOS,VACANTES)
    matchingGS(jugadores, equipos, JUGADORES, RUTA)
    for equipo in equipos.values():
        for jugador in equipo.getJugadores().values():
            descartados = jugador.getEquiposDescartados()
            for equipo_descartado in descartados:
                assert(equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador.getNumero()))
    print("Test 1: OK\n")

def testInestabilidadesGS():
    '''Prueba que nunca se dara en las asignaciones finales:
    Equipo1 tiene a Jugador1 asignado
    Equipo2 tiene a Jugador2 asignado
    Equipo1 prefiere a Jugador2 antes que a Jugador1
    Equipo2 prefiere a Jugador1 antes que a Jugador2'''
    jugadores, equipos = cargaDeArchivos(JUGADORES,EQUIPOS,VACANTES)
    matchingGS(jugadores, equipos, JUGADORES, RUTA)
    for equipo_original in equipos.values():
        for jugador_original in equipo_original.getJugadores().values():
            descartados = jugador_original.getEquiposDescartados()
            for equipo_descartado in descartados:
                for jugador_externo in equipos[equipo_descartado].getJugadores():
                    condicion1 = equipo_original.getPosicionFavoritoActual() <= equipo_original.getPreferencias().index(jugador_externo)
                    condicion2 = equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador_original.getNumero())
                    assert(condicion1 or condicion2)
    print("Test 2: OK\n")

def imprimirResultado(ruta):
    with open(ruta) as archivo:
        for linea in archivo:
            print(linea)

def main():
    jugadores, equipos = cargaDeArchivos(JUGADORES,EQUIPOS,VACANTES)
    matchingGS(jugadores, equipos, JUGADORES, RUTA)
    imprimirResultado(RUTA)

main()
testPreferenciasGS()
testInestabilidadesGS()
