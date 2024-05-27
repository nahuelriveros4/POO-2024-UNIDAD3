import csv
from classLadrillo import Ladrillo

class GestorLadrillo:
    __listaLadrillo: list
    def __init__(self):
        self.__listaLadrillo = []

    def agregarLadrillo(self, unLadrillo):
        self.__listaLadrillo.append(unLadrillo)

    def testArchivo(self):
        archivo = open('ladrillos.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                "Saltear Cabacera"
                bandera = False
            else:
                Cantidad=int(fila[0])
                ide=int(fila[1])
                kgMateriaPrima =float(fila[2])
                costo=float(fila[3])
                unLadrillo=Ladrillo(Cantidad,ide,kgMateriaPrima,costo)
                self.agregarLadrillo(unLadrillo)
        archivo.close()

    def agregarM(self,unMaterial, cantUsada):
        for i in range(len(self.__listaLadrillo)):
            if self.__listaLadrillo[i].getCant() == cantUsada:
                self.__listaLadrillo[i].agregarMaterial(unMaterial)

    def mostrarDatos(self, IDE):
        i=0
        band = False
        while not band and i < len(self.__listaLadrillo):
            if self.__listaLadrillo[i].getID() == IDE:
                band = True
                print(f"Costo del ladrillo: ${self.__listaLadrillo[i].getCosto()}")
                print(f"{self.__listaLadrillo[i].printMaterial()}")
            else:
                i+=1

    def MostrarCosto(self):
        costoTotal = 0
        for i in range(len(self.__listaLadrillo)):
            costoTotal = self.__listaLadrillo[i].getCosto() + self.__listaLadrillo[i].getCostoAD()
            print(f"Ladrillo {self.__listaLadrillo[i].getID()}")
            print(f"Costo Total: ${costoTotal}")

    def MostrarListado(self):
        print("N°ID       Material      Costo Asociado")
        for i in range(len(self.__listaLadrillo)):
            print(f"{self.__listaLadrillo[i].getID()}            {self.__listaLadrillo[i].getMat()}           ${self.__listaLadrillo[i].getCosto()}")
           


    def mostrar(self):
        for i in range(len(self.__listaLadrillo)):
            print(f"-----LADRILLO {self.__listaLadrillo[i].getID()}----")
            print(self.__listaLadrillo[i])
            print(self.__listaLadrillo[i].printMaterial())
            print("-----------------------------")