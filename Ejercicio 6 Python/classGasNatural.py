from classCalefactores import *
class GasNatural(Calefactores):
    __Matricula:str
    __Calorias:str
    def __init__(self, tipo, marca, modelo, pais, precioLista, formapago, cuotas, promocion, potenciaMax="", matricula="", calorias=""):
        super().__init__(tipo, marca, modelo, pais, precioLista, formapago, cuotas, promocion, potenciaMax, matricula, calorias)
        self.__Matricula = matricula
        self.__Calorias = calorias

    def __str__(self) -> str:
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Matricula: {self.__Matricula}\n"
                f"Calorias: {self.__Calorias}")
    
    def mostrarDatos(self):
        base  = super().mostrarDatos()
        return (f"{base}"
                f"Calorias: {self.__Calorias}")
    
    def calcular_importe_venta(self):
        precio_lista = self.getPrecioLista()
        importe_venta = precio_lista

        # Aplicar descuento por promoción
        if self.getPromocion == "Sí":
            importe_venta -= 0.15 * precio_lista

        # Reglas específicas para calefactores a gas natural
        calorias = int(self.__Calorias.split()[0])
        if calorias > 3000:
            importe_venta += 0.01 * precio_lista
        if self.getFormaDePago() == "cuotas":
            importe_venta += 0.40 * precio_lista

        return (f"Importe de venta: ${importe_venta}")
    
    def to_dict(self):
        data = super().to_dict()
        data["matricula"] = self.__Matricula
        data["calorias"] = self.__Calorias
        return data
