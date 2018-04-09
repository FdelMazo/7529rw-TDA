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
    with open(RUTA) as archivo:
        for linea in archivo:
            print(linea)
    for equipo in equipos.values():
        for jugador in equipo.getJugadores():
            descartados = jugador.getEquiposDescartados()
            for equipo_descartado in descartados:
                assert(equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador.getNumero()))
    print("OK\n")

def testInestabilidadesGS():
    '''Prueba que nunca se dara en las asignaciones finales:
    Equipo1 tiene a Jugador1 asignado
    Equipo2 tiene a Jugador2 asignado
    Equipo1 prefiere a Jugador2 antes que a Jugador1
    Equipo2 prefiere a Jugador1 antes que a Jugador2'''
    jugadores, equipos = cargaDeArchivos(JUGADORES,EQUIPOS,VACANTES)
    matchingGS(jugadores, equipos, JUGADORES, RUTA)
    with open(RUTA) as archivo:
        for linea in archivo:
            print(linea)
    for equipo_original in equipos.values():
        for jugador_original in equipo_original.getJugadores():
            descartados = jugador_original.getEquiposDescartados()
            for equipo_descartado in descartados:
                for jugador_externo in equipos[equipo_descartado].getJugadores():
                    condicion1 = equipo_original.getPosicionFavoritoActual() <= equipo_original.getPreferencias().index(jugador_externo.getNumero())
                    condicion2 = equipos[equipo_descartado].getPosicionFavoritoActual() <= equipos[equipo_descartado].getPreferencias().index(jugador_original.getNumero())
                    assert(condicion1 or condicion2)
    print("OK\n")

def main():
    ''' Llamada a la función de asignación.
    '''
    jugadores, equipos = cargaDeArchivos(JUGADORES,EQUIPOS,VACANTES)
    matchingGS(jugadores, equipos, JUGADORES, RUTA) #Cambiar a True si se quieren usar nuevos sets aleatorios

main()
testPreferenciasGS()
testInestabilidadesGS()
