from gestorEdificio import GestorEdificio

def opcion0(GE):
    print("Adios")

def opcion1(GE):
    nom = input("Ingrese 'Edificio Norte' o 'Edificio Sur': ")
    GE.mostrarDptos(nom)

def opcion2(GE):
    nom = input("Ingrese 'Edificio Norte' o 'Edificio Sur': ")
    GE.superficie(nom)

def opcion3(GE):
    nom = input("Ingrese nombre de un propietario: ")
    GE.superficePropietario(nom)

def opcion4(GE):
    piso = int(input("Ingrese numero de piso: "))
    GE.piso(piso)

switcher = {
    0:opcion0,
    1:opcion1,
    2:opcion2,
    3:opcion3,
    4:opcion4
}

def switch (opcion, GE):
    func = switcher.get(opcion, lambda: print("opcion incorrecta"))
    if opcion == 0 or opcion ==1 or opcion == 2 or opcion ==3 or opcion == 4:
        func(GE)
    else:
        func()

if __name__=='__main__':
    GE=GestorEdificio()
    GE.testArchivo()

    band = False
    while not band:
        print("\n----MENU----")
        print("1 - Mostrar propietarios de los departamentos")
        print("2 - Mostrar superficie total de un edificio")
        print("3 - Mostrar la superficie total cubierta de un propietario")
        print("4 - Mostrar la cantidad de departamentos que tienen 3 dormitorios y más de un baño")
        print("0 - SALIR")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion,GE)
        band = int(opcion) == 0