from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def instertarCalefactor(self, posicion, elemento):
        pass

    @abstractmethod
    def agregarCalefactor(self, elemento):
        pass

    @abstractmethod
    def mostrarCalefactor(self, posicion):
        pass

