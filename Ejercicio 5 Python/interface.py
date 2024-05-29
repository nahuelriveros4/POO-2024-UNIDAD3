from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def instertarElemento(self, posicion, elemento):
        pass

    @abstractmethod
    def agregarElemento(self, elemento):
        pass

    @abstractmethod
    def mostrarElemento(self, posicion):
        pass


    #Se crea la clase abstracta: 

    #Permite construir una interfaz común a un conjunto de subclases. Se construye para reunir un conjunto de atributos comunes al conjunto de subclases.
    
    #Es aquella que define una interfaz, pero no su implementación, de tal forma    que sus subclases sobrescriban los métodos con las implementaciones correspondientes.
    
    #Una clase abstracta no puede ser instanciada.