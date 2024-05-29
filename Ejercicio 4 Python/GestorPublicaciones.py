from classNodo import Nodo
from classLibro import *
from classCD import *

class ListaPublicaciones:
    __comienzo: Nodo
    def __init__(self):
        self.__comienzo =None
    
    def agregarLibro(self):
        print("\nCargar datos del libro")
        titulo = input("Ingrese titulo de la publicacion: ")
        categora = input("Ingrese categoria: ")
        precioBase = float(input("Ingrese Precio Base: "))
        autor = input("Ingrese nombre del autor: ")
        fecha = int(input("Ingrese año de edicion: "))
        pag = int(input("Ingrese cantidad de paginas: "))
        unLibro = Libro(titulo,categora,precioBase,autor,fecha,pag)
        nodo = Nodo(unLibro)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def agregarCD(self):
        print("\nCargar datos del CD")
        titulo = input("Ingrese titulo de la publicacion: ")
        categora = input("Ingrese categoria: ")
        precioBase = float(input("Ingrese Precio Base: "))
        tiemmp = float(input("Ingrese tiempo de reproduccion: "))
        narrador = input("Ingrese nombre del narrador: ")
        unCD = CD(titulo,categora,precioBase,0,0,0,tiemmp,narrador)
        nodo = Nodo(unCD)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def obtener_en_posicion(self, posicion):
        aux = self.__comienzo
        contador = 0
        valorRetorno = None
        while aux !=  None:
            if contador == posicion:
                valorRetorno = aux.getDatos()
            contador += 1
            aux = aux.getSiguiente()
        return valorRetorno  
    
    def mostrar_Tipo_Publicacion(self,posicion):
        publicacion = self.obtener_en_posicion(posicion)
        if publicacion == None:
            print(f"No hay ningun elemento en la posicion {posicion+1}")
        elif isinstance(publicacion, Libro):
            print(f"En la posición {posicion+1} se encuentra un Libro")
        else:
            if isinstance(publicacion, CD):
                print(f"En la posición {posicion+1} se encuentra un AudioLibro")
       
       
    def contar(self):
        contLibros = 0
        contCD = 0
        aux = self.__comienzo
        while aux != None:
            elemento = aux.getDatos()
            if isinstance(elemento,Libro):
                contLibros +=1
            else:
                if isinstance(elemento,CD):
                 contCD +=1
            aux = aux.getSiguiente()
        print(f"Cantidad de Libros: {contLibros}")
        print(f"Cantidad de AudioLibros: {contCD}")

    def recorrer(self):
        aux = self.__comienzo
        while aux != None:
            elemento = aux.mostrarRecorrer()
            print(elemento)
            aux = aux.getSiguiente()
        


    