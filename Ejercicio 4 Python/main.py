from GestorPublicaciones import ListaPublicaciones

def opcion0(lista):
    print("Adios")

def opcion1(lista):
    lista.agregarLibro()

def opcion2(lista):
    lista.agregarCD()

def opcion3(lista):
    posicion = int(input("Ingrese una posicion de la lista: "))
    if posicion > 0:
        lista.mostrar_Tipo_Publicacion(posicion-1)
    else:
        print("Posicion invalida (Ingrese mayor de 0)")

def opcion4(lista):
    lista.contar()

def opcion5(lista):
    lista.recorrer()

swicher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5
}

def switch(opcion, lista):
    func = swicher.get(opcion, lambda:print("Opcion incorrecta"))
    if opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
        func(lista)
    else:
        func()


if __name__ == '__main__':
    lista = ListaPublicaciones ()
    

    bandera = False
    while not bandera:
        print("\n-----MENU------")
        print("1 - Agregar Libros")
        print("2 - Agregar CDs")
        print("3 - Mostrar tipo de publicacion")
        print("4 - Mostrar cantidad de publicaciones de cada tipo")
        print("5 - Mostrar ' Titulo, categoría e importe de venta.' de todas las publicaciones")
        print("0 - Salir")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion, lista)
        bandera = int(opcion) == 0