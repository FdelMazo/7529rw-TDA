from EntidadConPreferencias import EntidadConPreferencias

class Jugador(EntidadConPreferencias):

    def __init__(self, numeroJugador, preferenciasJugador):
        '''Constructor.
        Pre: numeroJugador es un número natural.
             preferenciasJugador es una lista de números naturales.
        Post: se creo el jugador.'''
        diccPreferencias = {}
        for i, equipo in enumerate(preferenciasJugador[::-1]):
            diccPreferencias[equipo] = i
        EntidadConPreferencias.__init__(self,numeroJugador, diccPreferencias)
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

    def getEquiposDescartados(self):
        prioridad_asignada = self.preferencias[self.lugarAsignado.getNumero()]
        aux = []
        for equipo in self.preferencias.keys():
            if self.preferencias[equipo] > prioridad_asignada:
                aux.append(equipo)
        return aux

    def compararPreferencias(self, equipo1, equipo2):
        return self.preferencias[equipo1.getNumero()] > self.preferencias[equipo2.getNumero()]
        '''for preferencia in self.preferencias:
            if equipo1.getNumero() == preferencia: return 1
            elif equipo2.getNumero() == preferencia: return -1
         #Nunca debería ser cero'''