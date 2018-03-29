from EntidadConPreferencias import EntidadConPreferencias

class Jugador(EntidadConPreferencias):
    
    def __init__(self, numeroJugador, preferenciasJugador):
        '''
        Constructor.
        Pre: numeroJugador es un número natural.
             preferenciasJugador es una lista de números naturales.
        Post: se creo el jugador.
        '''
        EntidadConPreferencias.__init__(self,numeroJugador, preferenciasJugador)
        self.asignado = False
        self.lugarAsignado = None
    
    def getAsignado(self):
        return self.asignado
    
    def setAsignado(self, valor):
        self.asignado = valor
        
    def getLugarAsignado(self):
        return self.lugarAsignado
    
    def setLugarAsignado(self, lugar):
        self.lugarAsignado = lugar
    
    def estaAsignado(self):
        return self.asignado
    
    def asignar(self, lugar):
        self.asignado = True
        self.lugarAsignado = lugar
    
    def desasignar(self):
        self.asignado = False
        self.lugarAsignado = None
    
    def compararPreferencias(self, num1, num2):
        for p in self.preferencias:
            if num1 == p: return 1
            elif num2 == p: return -1
    '''Nunca debería ser cero '''
