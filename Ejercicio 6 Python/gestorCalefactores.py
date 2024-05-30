from nodo import Nodo
from interface import *
import json
from classElectrico import *
from classGasNatural import *

class ListaCalefactores(Interface):
    __comienzo: Nodo
    def __init__(self):
        self.__comienzo = None
        
    def instertarCalefactor(self, posicion, elemento):
        nuevo_nodo = Nodo(elemento)
        if posicion == 0:
            nuevo_nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
        else:
            actual = self.__comienzo
            contador = 0
            while actual and contador < posicion-1:
                actual = actual.getSiguiente()
                contador += 1
            if actual is None:
                raise IndexError("La posición excede el tamaño de la lista")
            nuevo_nodo.setSiguiente(actual.getSiguiente()) 
            actual.setSiguiente(nuevo_nodo)


    def insertar(self, posicion):
        tipo = input("Ingrese tipo de calefactor 'electrico' o 'gas natural': ")
        marca = input("Ingrese marca: ")
        modelo = input("Ingrese Modelo: ")
        pais = input("Ingrese Pais: ")
        precioLista = float(input("Ingrese precio de lista: "))
        formapago = input("Ingrese forma de pago (contado o cuotas): ")
        cuotas = int(input("Ingrese cantidad de cuotas (1 si es de contado): "))
        promocion = input("Calefactor en promocion (Si o No): ")
        if tipo == "electrico":
            potenciaMax = input("Ingrese potencia maxima: ")
            unElectrico= Electrico(tipo,marca,modelo,pais,precioLista,formapago,cuotas,promocion,potenciaMax)
            if posicion == 0:
                self.agregarCalefactor(unElectrico)
            else:
                self.instertarCalefactor(posicion, unElectrico)
        else: 
            if tipo == "gas natural":
                Matricula = input("Ingrese matricula: ")
                Calorias = input("Ingrese calorias: ")
                unGasNatural = GasNatural(tipo,marca,modelo,pais,precioLista,formapago,cuotas,promocion,0,Matricula,Calorias)
                if posicion == 0:
                    self.agregarCalefactor(unGasNatural)
                else:
                    self.instertarCalefactor(posicion, unGasNatural)


    def agregarCalefactor(self, calefactor):
        nodo = Nodo(calefactor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def testArchivo(self):
        with open("calefactores.json", "r") as file:
            calefactores = json.load(file)
        for calefactor in calefactores:
            if calefactor["tipo"] == "electrico":
                unElectrico = Electrico(calefactor["tipo"], calefactor["marca"], calefactor["modelo"],
                                               calefactor["pais_fabricacion"], calefactor["precio_lista"],
                                               calefactor["forma_pago"], calefactor["cantidad_cuotas"],
                                               calefactor["promocion"], calefactor["potencia_maxima"])
                self.agregarCalefactor(unElectrico)
            elif calefactor["tipo"] == "gas natural":
                unoGasNatural = GasNatural(calefactor["tipo"], calefactor["marca"], calefactor["modelo"],
                                                calefactor["pais_fabricacion"], calefactor["precio_lista"],
                                                calefactor["forma_pago"], calefactor["cantidad_cuotas"],
                                                calefactor["promocion"], 0,calefactor["matricula"], calefactor["calorias"])
                self.agregarCalefactor(unoGasNatural)
        file.close()

    def mostrarCalefactor(self, posicion):
        actual = self.__comienzo
        contador = 0
        band = False
        while actual and not band:
            if posicion -1 == contador:
                band=True
                if isinstance(actual.getDatos(),Electrico):
                    print(f"El elemento que se encuentra en la posicion {posicion} es un Calefactor Electrico")
                elif isinstance (actual.getDatos(),GasNatural):
                    print(f"El elemento que se encuentra en la posicion {posicion} es un Calefactor de Gas Natural")
            else:
                actual = actual.getSiguiente()
                contador += 1


    def menorPrecio(self):
        actual = self.__comienzo
        calefactor_menor_precio = None
        minimo = float('inf')
        while actual:
            dato = actual.getDatos()
            if isinstance(dato, GasNatural):
                if dato.getPrecioLista() < minimo:
                    minimo = dato.getPrecioLista()
                    calefactor_menor_precio = actual
            actual = actual.getSiguiente()
        if calefactor_menor_precio:
            print(f"El calefactor a gas natural con menor precio es: \n{calefactor_menor_precio.mostrarDatosGas()}")
        else:
            print("No se encontraron calefactores a gas natural en la lista.")


        
    def mostrarporMarca(self, marca):
        actual = self.__comienzo
        while actual:
            dato = actual.getDatos()
            if isinstance(dato, Electrico):
                if dato.getMarca() == marca:
                    print(f"\n{actual.mostrarDatosElec()}")
            actual = actual.getSiguiente()

    def mostrarPromocion(self):
        actual = self.__comienzo
        while actual:
            dato = actual.getDatos()
            if dato.getPromocion() == 'Si':
                print(f"\n{actual.mostrarPromo()}")
                print(f"{actual.importe()}")
            actual = actual.getSiguiente()

    def almacenarDatos(self):
        actual = self.__comienzo
        Calefactor = []
        while actual:
            Calefactor.append(actual.getDatos().to_dict())
            actual = actual.getSiguiente()
        with open('calefactores.json', 'w') as archivo_json:
            json.dump(Calefactor, archivo_json, indent=4)
            archivo_json.close()

