from EntidadConPreferencias import EntidadConPreferencias

class Equipo(EntidadConPreferencias):
    
    def __init__(self, numeroEquipo, preferenciasEquipo, vacantesInicialEquipo):
        '''
        Constructor.
        Pre: numeroEquipo y capacidadInicialEquipo son números naturales.
             preferenciasEquipo es una lista de números naturales.
        Post: se creo el equipo.
        '''
        EntidadConPreferencias.__init__(self,numeroEquipo, preferenciasEquipo)
        self.vacantes = vacantesInicialEquipo
        self.jugadores = []
    
    def getVacantes(self):
        return self.vacantes
    
    def setVacantes(self, capacidadInicialEquipo):
        self.vacantes = capacidadInicialEquipo
    
    def setJugadores(self, jugadoresEquipo):
        self.jugadores = jugadoresEquipo
        
    def getJugadores(self):
        return jugadoresEquipo
    
    def getFavorito(self):
        return self.preferencias[self.posicionFavoritoActual]
    
    def setearProximoFavorito(self): 
        self.posicionFavoritoActual += 1
        ''' Nunca deberia salirse del límite de la lista '''
        
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)
        jugador.asignar(self)
        self.vacantes -= 1
    
    def quitarJugador(self, jugador):
        self.jugadores.remove(jugador)
        jugador.desasignar()
        self.vacantes +=1