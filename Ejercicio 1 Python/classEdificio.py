from classDepto import Departamento

class Edificio:
    __id:int
    __Nombre: str
    __Direccion:str
    __NomEmpresa:str
    __CantPiso:int
    __CantidadDptos:int
    __listaDeptos:list
    def __init__(self, ide,nom,direc,empresa,cantpiso,cantdptos):
        self.__id= ide
        self.__Nombre = nom
        self.__Direccion = direc
        self.__NomEmpresa = empresa
        self.__CantPiso= cantpiso
        self.__CantidadDptos = cantdptos
        self.__listaDeptos = []
    
    def __str__(self):
        return (f"ID: {self.__id}\n"
                f"Nombre: {self.__Nombre}\n"
                f"Dirección: {self.__Direccion}\n"
                f"Nombre de la Empresa: {self.__NomEmpresa}\n"
                f"Cantidad de Pisos: {self.__CantPiso}\n"
                f"Cantidad de Departamentos: {self.__CantidadDptos}\n")


    def agregarDpto(self, unDpto):
        self.__listaDeptos.append(unDpto)
    
    def getID(self):
        return self.__id
    
    def getNombre(self):
        return self.__Nombre
    
    def mostrarDpto(self):
        print(f"---LISTA DPTOS {self.__Nombre}----")
        for i in range(len(self.__listaDeptos)):
            print(self.__listaDeptos[i])
            print(f"-------------")


    def mostrarDpto2 (self, ide):
       for i in range(len(self.__listaDeptos)):
           if self.__listaDeptos[i].getIDE() == ide:
               print("---------------")
               print(f"Propietario: {self.__listaDeptos[i].getNom()}")
               print(f"Piso: {self.__listaDeptos[i].getPiso()}")
               print(f"Depto: {self.__listaDeptos[i].getNumeroDpto()}")

    def superficie(self, IDe):
        cont=0
        for i in range(len(self.__listaDeptos)):
            if self.__listaDeptos[i].getIDE() == IDe:
                cont += self.__listaDeptos[i].getSup()
        print(f"Supercie cubierta: {cont}m²")

    def sup(self, nompr, nomed):
        cont=0
        cont2 = 0
        for i in range(len(self.__listaDeptos)):
            cont2 += self.__listaDeptos[i].getSup()
            if self.__listaDeptos[i].getNom() == nompr:
                cont += self.__listaDeptos[i].getSup()
        porcentaje = (cont * 100)/cont2
        print(f"Superficie cubierta en el {nomed} por el/los departamentos de {nompr} es de {cont}m² y representa el %{porcentaje:.2f}")

    def pisos(self, numpiso, nomEdif):
        cont = 0
        for i in range(len(self.__listaDeptos)):
            if self.__listaDeptos[i].getHabitacion() == 3 and self.__listaDeptos[i].getBaños() > 1 and self.__listaDeptos[i].getPiso() == numpiso:
                cont +=1
        print(f"El edificio {nomEdif} en el piso N°{numpiso} cuenta con {cont} departamentos que cuentan con 3 dormitorios y mas de un baño")
