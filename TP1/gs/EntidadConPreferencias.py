class EntidadConPreferencias:
    
    def __init__(self, numero, preferencias):
        '''
        Constructor.
        Pre: numero es un número natural.
             preferencias es una lista de números naturales.
        Post: se creo la entidad.
        '''
        self.numero = numero
        self.preferencias = preferencias
        self.posicionFavoritoActual = 0
    
    def setNumero(self, numero):
        self.numero = numero
    
    def setPreferencias(self, preferencias):
        self.preferencias = preferencias
    
    def getNumero(self):
        return self.numero

    def getPreferencias(self):
        return self.preferencias
    
    def getPosicionFavoritoActual(self):
        return posicionFavoritoActual
    
    def setPosicionFavoritoActual(self, posicionFavoritoActual):
        self.posicionFavoritoActual = posicionFavoritoActual