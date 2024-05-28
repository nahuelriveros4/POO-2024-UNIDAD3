from classPrograma import Programa
import csv

class GestorPrograma:
    __listaProgramas:list
    def __init__(self):
        self.__listaProgramas = []
    
    def agreagarPrograma(self, unPrograma):
        self.__listaProgramas.append(unPrograma)

    def testArchivo(self):
        archivo = open('programa.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                "saltear Cabecera"
                bandera = not bandera
            else:
                unPrograma=Programa(fila[0], fila[1], fila[2])
                self.agreagarPrograma(unPrograma)
        archivo.close()

    
    def buscarPrograma(self, nombre):
        i=0
        band = False
        while not band and i < len(self.__listaProgramas):
            if self.__listaProgramas[i].getNom() == nombre:
                band = True
                return (self.__listaProgramas[i])
            else:
                i+=1
        return None

    def mostrarEmpleados(self, nom):
        i=0
        band = False
        while not band and i < len(self.__listaProgramas):
            if self.__listaProgramas[i].getNom() == nom:
                band = True
                self.__listaProgramas[i].mostrarEmp()
            else:
                i+=1 


    def mostrar(self):
        print("------------------PROGRAMAS---------------")
        for i in range(len(self.__listaProgramas)):
            print(self.__listaProgramas[i])
            print("---------------------------------")