class Calefactores(object):
    __Tipo: str
    __Marca: str
    __Modelo: str
    __Pais:str
    __PrecioLista:float
    __FormadePago:str
    __CantidadCuotas: int
    __Promocion:str
    def __init__(self, tipo,marca,modelo,pais,precioLista,formapago,cuotas,promocion, potenciaMax="", matricula="", calorias=""):
        self.__Tipo = tipo
        self.__Marca =marca
        self.__Modelo = modelo
        self.__Pais = pais
        self.__PrecioLista = precioLista
        self.__FormadePago = formapago
        self.__CantidadCuotas = cuotas
        self.__Promocion = promocion

    def __str__(self) -> str:
        return (f"Tipo: {self.__Tipo}\n"
                f"Marca: {self.__Marca}\n"
                f"Modelo: {self.__Modelo}\n"
                f"Pais: {self.__Pais}\n"
                f"Precio Lista: {self.__PrecioLista}\n"
                f"Forma de Pago: {self.__FormadePago}\n"
                f"Cuotas: {self.__CantidadCuotas}\n"
                f"Promocion: {self.__Promocion}")
    
    def getPrecioLista(self):
        return self.__PrecioLista
    
    def mostrarDatos(self):
        return (f"Marca: {self.__Marca}\n"
                f"Modelo: {self.__Modelo}\n")
    
    def mostrarDatosElectrico(self):
        return (f"Modelo: {self.__Modelo}\n"
                f"Precio Lista: {self.__PrecioLista}\n")
    
    def getMarca(self):
        return self.__Marca
    
    def getFormaDePago(self):
        return self.__FormadePago
    
    def getPromocion(self):
        return self.__Promocion
    
    def mostrarDatoPromo(self):
        return (f"Marca: {self.__Marca}\n"
                f"Modelo: {self.__Modelo}\n"
                f"Pais: {self.__Pais}")

    def calcular_importe_venta(self):
        pass
        #se sobreescribe en las subclases

    def to_dict(self):
        return {
            "tipo": self.__Tipo,
            "marca": self.__Marca,
            "modelo": self.__Modelo,
            "pais_fabricacion": self.__Pais,
            "precio_lista": self.__PrecioLista,
            "forma_pago": self.__FormadePago,
            "cantidad_cuotas": self.__CantidadCuotas,
            "promocion": self.__Promocion
        }


    
