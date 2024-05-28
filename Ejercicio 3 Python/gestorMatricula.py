from classMatricula import Matricula
from gestorEmpleado import *
from gestorPrograma import *
import csv

class GestorMartricula:
    __listaMatriculas:list
    def __init__(self):
        self.__listaMatriculas = []
    
    def agregarMatricular(self, unaMatricula):
        self.__listaMatriculas.append(unaMatricula)

    def testArchivo(self,GE,GP):
        archivo = open('matriculas.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                "saltear Cabecera"
                bandera = not bandera
            else:
                unaMatricula=Matricula(fila[0],GE.buscarEmpleado(int(fila[1])),GP.buscarPrograma(fila[2]))
                self.agregarMatricular(unaMatricula)
        archivo.close()


    def mostrar(self):

        print("---------------MATRICULAS------------------")
        for i in range(len(self.__listaMatriculas)):
            
            print(self.__listaMatriculas[i])
            print("---------------------------------")
            