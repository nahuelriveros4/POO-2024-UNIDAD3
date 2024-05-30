from gestorCalefactores import *

def opcion0(lista):
    print("Adios")

def opcion1(lista):
    posicion = int(input("Ingrese posicion: "))
    lista.insertar(posicion)

def opcion2(lista):
    lista.insertar(0)

def opcion3(lista):
    posicion = int(input("Ingrese posicion: "))
    lista.mostrarCalefactor(posicion)

def opcion4(lista):
    lista.menorPrecio()

def opcion5(lista):
    marca = input("Ingrese Marca: ")
    lista.mostrarporMarca(marca)

def opcion6(lista):
    lista.mostrarPromocion()

def opcion7(lista):
    lista.almacenarDatos()
    print("Datos cargados correctamente")


switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
    6: opcion6,
    7: opcion7
}

def switch (opcion, lista):
    func = switcher.get(opcion, lambda: print("Opcion incorrecta"))
    if opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 7:
        func(lista)
    else:
        func()

if __name__ == '__main__':
    lista = ListaCalefactores()
    lista.testArchivo()

    band = False
    while not band:
        print("\n-------MENU------")
        print("1 - Insertar un calefactor en una posicion")
        print("2 - Agregar un calefactor")
        print("3 - Mostrar tipo de objeto que se encuentra en una posicion")
        print("4 - Mostrar marca, modelo y kilocalorías del calefactor a gas natural de menor precio.")
        print("5 - Mostrar Calefactor Electrico por marca")
        print("6 - Mostrar Datos de calefactores en promocion")
        print("7 - Almacenar los datos en un archivo json")
        print("0 - Salir ")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion, lista)
        band = int(opcion) == 0