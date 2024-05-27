from classMaterial import Material
import csv

class GestorMaterial:
    __listaMateriales: list
    def __init__(self) :
        self.__listaMateriales = []

    def agregarMaterial(self,unMaterial):
        self.__listaMateriales.append(unMaterial)

    def testArchivo(self):
        archivo = open('material.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                "saltear cabecera"
                bandera = False
            else:
                Mat= int(fila[0])
                Caracteristicas= fila[1]
                CantidadUsada= float(fila[2])
                CostoAdicional= float(fila[3])
                unMaterial = Material(Mat,Caracteristicas,CantidadUsada,CostoAdicional)
                self.agregarMaterial(unMaterial)
        archivo.close()

    def agregarMat(self, GL):
        for i in range(len(self.__listaMateriales)):
            cant = self.__listaMateriales[i].getCant()
            GL.agregarM(self.__listaMateriales[i], cant)


    def mostrar(self):
        print("-----------------------------")
        for i in range(len(self.__listaMateriales)):
            print(self.__listaMateriales[i])
            print("-----------------------------")
    
