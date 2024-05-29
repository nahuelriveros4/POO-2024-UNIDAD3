from classPublicaciones import Publicaciones
class Nodo:
    __Publicacion: Publicaciones
    __siguiente : object
    def __init__(self,public):
        self.__Publicacion = public
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDatos(self):
        return self.__Publicacion
    
    def mostrarRecorrer(self):
        return self.__Publicacion.mostrarDatos()

