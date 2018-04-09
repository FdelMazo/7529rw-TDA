class EntidadConPreferencias:

    def __init__(self, numero, preferencias):
        '''Constructor.
        Pre: numero es un número natural.
             preferencias es una lista de números naturales.
        Post: se creo la entidad.'''
        self.numero = numero
        self.preferencias = preferencias
        self.posicionFavoritoActual = 0

    def setNumero(self, numero):
        ''' Setea el número de entidad.
        Pre: numero es un número natural.
        Post: el número fue asignado.
        '''
        self.numero = numero

    def setPreferencias(self, preferencias):
        ''' Setea las preferencias de la entidad.
        Pre: preferencias es una lista de números naturales.
        Post: la lista fue asignada.
        '''
        self.preferencias = preferencias

    def setPosicionFavoritoActual(self, posicionFavoritoActual):
        ''' Asigna la posición en la lista de preferencias de la entidad.
        '''
        self.posicionFavoritoActual = posicionFavoritoActual

    def getNumero(self):
        ''' Devuelve el número de entidad.
        '''
        return self.numero

    def getPreferencias(self):
        ''' Devuelve las preferencias de la entidad.
        '''
        return self.preferencias

    def getPosicionFavoritoActual(self):
        ''' Devuelve la posición de mayor preferencia
        de la entidad dentro de su lista de preferencias.
        Incluso si la lista está vacia, devuelve el valor
        inicial asignado al inicializar la entidad.
        '''
        return self.posicionFavoritoActual
