from coleccion import *
def test():
    coleccion = Coleccion()
    coleccion.agregarElemento("Elemento 1")
    coleccion.agregarElemento("Elemento 2")
    coleccion.agregarElemento("Elemento 3")
    coleccion.instertarElemento(2, "Elemento 2.5")
    coleccion.mostrarElemento(2) #debe mostrar "elemento 2.5"
    
    #Insertar en posicion invalida
    coleccion.instertarElemento(10, "Elemento Fuera de Rango")

    # Intentar mostrar un elemento en una posición inválida
    coleccion.mostrarElemento(10)

if __name__ == '__main__':
    test()
