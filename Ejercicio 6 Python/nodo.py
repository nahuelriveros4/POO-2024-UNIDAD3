from classCalefactores import *
class Nodo:
    __Calefactor : Calefactores
    __siguiente = None
    def __init__(self, calefactor):
        self.__Calefactor = calefactor
        self.__siguiente = None
    
    def getDatos(self):
        return self.__Calefactor
    
    def setSiguiente(self, calefactor):
        self.__siguiente = calefactor

    def getSiguiente(self):
        return self.__siguiente

    def mostrarDatosGas(self):
        return self.__Calefactor.mostrarDatos()
    
    def precio(self):
        return self.__Calefactor.getPrecioLista()
    
    def mostrarDatosElec(self):
        return self.__Calefactor.mostrarDatosElectrico()
    
    def mostrarPromo(self):
        return self.__Calefactor.mostrarDatoPromo()
    
    def importe(self):
        return self.__Calefactor.calcular_importe_venta()