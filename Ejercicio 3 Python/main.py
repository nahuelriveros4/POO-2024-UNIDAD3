from gestorEmpleado import GestorEmpleado
from gestorMatricula import GestorMartricula
from gestorPrograma import GestorPrograma

def opcion0(GE,GM,GP):
    print("Adios")

def opcion1(GE,GM,GP):
    ide = int(input("Ingrese ID del empleado: "))
    GE.informarDuracion(ide)

def opcion2(GE,GM,GP):
    nom = input("Ingrese nombre del programa: ")
    GP.mostrarEmpleados(nom)

def opcion3(GE,GM,GP):
    GE.empleadoSinMatricular()

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch (opcion, GE,GM,GP):
    func = switcher.get(opcion, lambda:print("Opcion incorrecta"))
    if opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3:
        func (GE,GM,GP)
    else:
        func()




if __name__ == '__main__':
    GE = GestorEmpleado()
    GM = GestorMartricula()
    GP = GestorPrograma()
    GE.testArchivo()
    GP.testArchivo()
    GM.testArchivo(GE,GP)
    
    #GE.mostrar()
    #GM.mostrar()
    #GP.mostrar()

    band = False
    while not band:
        print("\n-----MENU------")
        print("1 - Dado el Id del empleado, informe la duración de todos los programas decapacitación en los que está matriculado.")
        print("2 - Dado el nombre de un programa de capacitación, muestre el/los empleados matriculados en el mismo.")
        print("3 - Informar aquellos Empleados que no han sido matriculados en ningún programa de capacitación")
        print("0 - Salir")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion,GE,GM,GP)
        band = int(opcion) == 0