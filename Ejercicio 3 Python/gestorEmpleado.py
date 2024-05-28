from classEmpleado import Empleado
import csv

class GestorEmpleado:
    __listaEmpleados:list
    def __init__(self):
        self.__listaEmpleados = []

    def agregarEmpleado(self, unEmpleado):
        self.__listaEmpleados.append(unEmpleado)

    def testArchivo(self):
        archivo = open('empleados.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                "saltear Cabecera"
                bandera = not bandera
            else:
                unEmpleado=Empleado(fila[0],int(fila[1]),fila[2])
                self.agregarEmpleado(unEmpleado)
        archivo.close() 
    
    def buscarEmpleado(self, ide):
        i=0
        band = False
        while not band and i< len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getID() == ide:
                band = True
                return self.__listaEmpleados[i]
            else:
                i+=1
        return None
    
    def informarDuracion(self, ide):
        i = 0
        band = False
        while not band and i<len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getID() == ide:
                band = True
                self.__listaEmpleados[i].mostrarDuracion()
            else:
                i+=1

    def empleadoSinMatricular (self):
        for i in range(len(self.__listaEmpleados)):
            self.__listaEmpleados[i].mostrarMatriculas()

    def mostrar(self):
        print("---------------EMPLEADOS------------------")
        for i in range(len(self.__listaEmpleados)):
            print(self.__listaEmpleados[i])
            print("-----Matricula------")
            self.__listaEmpleados[i].printMatricula()
            print("---------------------------------")
            print("---------------------------------")