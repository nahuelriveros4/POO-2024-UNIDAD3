from classCalefactores import * 
class Electrico(Calefactores):
    __PotenciaMaxima : str
    def __init__(self, tipo, marca, modelo, pais, precioLista, formapago, cuotas, promocion, potenciaMax="", matricula="", calorias=""):
        super().__init__(tipo, marca, modelo, pais, precioLista, formapago, cuotas, promocion, potenciaMax, matricula, calorias)
        self.__PotenciaMaxima = potenciaMax

    def __str__(self) -> str:
        base_str = super().__str__()
        return(f"{base_str}\n"
               f"Potencia Max: {self.__PotenciaMaxima}")
    
    def mostrarDatosElectrico(self):
        base= super().mostrarDatosElectrico()
        return(f"{base}"
               f"Potencia: {self.__PotenciaMaxima}\n")

    def calcular_importe_venta(self):
        precio_lista = self.getPrecioLista()
        importe_venta = precio_lista

        # Aplicar descuento por promoción
        if self.getPromocion() == "Sí":
            importe_venta -= 0.15 * precio_lista

        # Reglas específicas para calefactores eléctricos
        potencia_maxima = int(self.__PotenciaMaxima.split()[0])
        if potencia_maxima > 1000:
            importe_venta += 0.01 * precio_lista
        if self.getFormaDePago() == "cuotas":
            importe_venta += 0.30 * precio_lista

        return (f"Importe de venta: ${importe_venta}")
    
    def to_dict(self):
        data = super().to_dict()
        data["potencia_maxima"] = self.__PotenciaMaxima
        return data