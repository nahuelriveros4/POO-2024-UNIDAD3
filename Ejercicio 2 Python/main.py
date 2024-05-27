from gestorLadrillo import GestorLadrillo
from gestorMaterial import GestorMaterial

def opcion0(GM,GL):
    print("Exit")

def opcion1(GM,GL):
    ide = int(input("Ingrese ID del ladrillo: "))
    GL.mostrarDatos(ide)

def opcion2(GM,GL):
    GL.MostrarCosto()

def opcion3(GM,GL):
    GL.MostrarListado()

swtcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(opcion,GM,GL):
    func = swtcher.get(opcion, lambda:print("Opcion incorrecta"))
    if opcion == 0 or opcion ==1 or opcion == 2 or opcion == 3:
        func(GM,GL)
    else:
        func()


if __name__ == '__main__':
    GM = GestorMaterial()
    GL = GestorLadrillo()
    GL.testArchivo()
    GM.testArchivo()
    GM.agregarMat(GL)
    #GL.mostrar()

    bandera = False
    while not bandera:
        print("\n-------MENU--------")
        print("1 - Detalle del costo y material de un ladrillo")
        print("2 - Mostrar costo total de fabricacion de un ladrillo")
        print("3 - Mostrar detalle de cada ladrillo")
        print("0 - EXIT")
        opcion = int(input("Ingrese una opcion: "))
        switch(opcion,GM,GL)
        bandera = int(opcion) == 0
