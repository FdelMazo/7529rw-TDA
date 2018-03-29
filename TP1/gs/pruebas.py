from Jugador import Jugador
from Equipo import Equipo

def probar(mensaje, condicion):
    if condicion:
        print(mensaje + ': OK')
    else:
        print(mensaje + ': NOOK')
        input()

def pruebasJugador():
    jugador = Jugador(1, '3,1,2')
    equipo = Equipo(1, '2,1',2)
    equipo2 = Equipo(2, '1,2',2)
    
    '''
    print('\n VER PREFERENCIAS \n')
    pref = jugador.getPreferencias()
    for p in pref:
        print(p)
    
    print('\nASIGNAR UN JUGADOR')
    jugador.asignar(equipo)
    probar('Esta bien asignado?', jugador.getLugarAsignado() == equipo)
    probar('Esta ocupado?', jugador.estaAsignado())
    
    print('\nDESASIGNAR UN JUGADOR')
    jugador.desasignar()
    probar('Esta desocupado?', not jugador.estaAsignado())   
    if not jugador.estaAsignado():
        equipo2.agregarJugador(jugador)
        equipo2.setearProximoFavorito()
    
    print('\nASIGNAR A UN JUGADOR DESDE UN EQUIPO')
    probar('Esta bien asignado?', jugador.getLugarAsignado() == equipo2)
    probar('Esta ocupado?', jugador.estaAsignado())
    probar('Favorito actual?',equipo2.getFavorito()==2)
    
    print('\nDESASIGNAR A UN JUGADOR DESDE UN EQUIPO')
    equipo2.quitarJugador(jugador)
    probar('Esta bien asignado?', jugador.getLugarAsignado() == None)
    probar('Esta ocupado?', not jugador.estaAsignado())
    probar('Favorito actual?',equipo2.getFavorito()==2)
    '''
    print('\nCAMBIO DE PREFERENCIA DE UN JUGADOR')
    equipo2.agregarJugador(jugador)
    probar('Esta ocupado?', jugador.estaAsignado())
    if jugador.compararPreferencias(equipo.getNumero(), jugador.getLugarAsignado().getNumero()) > 0:
        jugador.getLugarAsignado().quitarJugador(jugador)
        equipo.agregarJugador(jugador)
    probar('Esta ocupado?', jugador.estaAsignado())
    probar('Esta bien asignado?', jugador.getLugarAsignado() == equipo)
    
pruebasJugador()
