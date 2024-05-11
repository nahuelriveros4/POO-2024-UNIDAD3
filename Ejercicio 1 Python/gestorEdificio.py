from classDepto import Departamento
from classEdificio import Edificio
import csv

class GestorEdificio:
    __listaEdificio:list
    def __init__(self):
        self.__listaEdificio = []

    def agregarEdificio(self,edi):
        self.__listaEdificio.append(edi)

    def testArchivo(self):
        archivo = open('EdificioNorte.csv')
        reader = csv.reader(archivo,delimiter=";")
        aux=0
        for fila in reader:
            if aux != fila[0]:
                aux = fila[0]
                ide =  int(fila[0])
                Nombre = fila[1]
                Direccion = fila[2]
                NomEmpresa = fila[3]
                CantPiso= int(fila[4])
                CantidadDptos = int(fila[5])
                unEdi = Edificio(ide,Nombre,Direccion,NomEmpresa,CantPiso,CantidadDptos)
                self.agregarEdificio(unEdi)
            else:
                    idEdificio= int(fila[0])
                    idDpto = int(fila[1])
                    NomyAp= fila[2]
                    NumeroPiso=int(fila[3])
                    NumDpto=int(fila[4])
                    CantHabit=int(fila[5])
                    CantBaños=int(fila[6])
                    Sup=float(fila[7])
                    unDpto = Departamento(idEdificio,idDpto,NomyAp,NumeroPiso,NumDpto,CantHabit,CantBaños,Sup)
                    self.__listaEdificio[int(aux)-1].agregarDpto(unDpto)
        archivo.close()


    def mostrarDptos(self, nom):
        i = 0
        band = False
        while not band and i < len(self.__listaEdificio):
            if self.__listaEdificio[i].getNombre() == nom:
                band = True
                self.__listaEdificio[i].mostrarDpto2(self.__listaEdificio[i].getID())
            else:
                i+=1

    def superficie(self, nomb):
        i = 0
        band = False
        while not band and i < len(self.__listaEdificio):
            if self.__listaEdificio[i].getNombre() == nomb:
                band = True
                self.__listaEdificio[i].superficie(self.__listaEdificio[i].getID())
            else:
                i+=1

    def superficePropietario(self,nom):
        for i in range(len(self.__listaEdificio)):
            self.__listaEdificio[i].sup(nom, self.__listaEdificio[i].getNombre())

    def piso (self, numPiso):
        if numPiso > 0 and numPiso < 3:
            for i in range(len(self.__listaEdificio)):
                self.__listaEdificio[i].pisos(numPiso, self.__listaEdificio[i].getNombre())
        else:
            print("Numero de Piso invalido")


    def mostrar(self):
        print("----- EDIFICIO -----")
        for i in range(len(self.__listaEdificio)):
            print(f"{self.__listaEdificio[i]}")
            self.__listaEdificio[i].mostrarDpto()