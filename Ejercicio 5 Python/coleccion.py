from interface import Interface
class Coleccion(Interface):
    __coleccion:list
    def __init__(self):
        self.__coleccion = []

    def instertarElemento(self, posicion, elemento):
        try:
            if posicion < 0 or posicion > len(self.__coleccion):
                raise TypeError
            self.__coleccion.insert(posicion,elemento)
        except TypeError:
            print(f"Error al insertar elemento: {elemento}")


    def agregarElemento(self, elemento):
        self.__coleccion.append(elemento)

    
    def mostrarElemento(self, posicion):
        try:
            if posicion < 0 or posicion >= len(self.__coleccion):
               raise TypeError
            print (self.__coleccion[posicion])
        except TypeError:
            print(f"Error al mostrar el elemento de la posicion: {posicion}")


    #Se crea la subClase que sobresciben los metodos 