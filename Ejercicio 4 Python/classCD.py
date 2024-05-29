from classPublicaciones import Publicaciones
from datetime import datetime
class CD(Publicaciones):
    __TiempoReproduccion:float
    __Narrador: str
    def __init__(self, titulo, categoria, preciobase, autor="", fechaEdicion="", cantidadPaginas=0, tiempoReproduccion=0, narrador=""):
        super().__init__(titulo, categoria, preciobase, autor, fechaEdicion, cantidadPaginas, tiempoReproduccion, narrador)
        self.__TiempoReproduccion = tiempoReproduccion
        self.__Narrador = narrador
    
    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Tiempo de Reproduccion: {self.__TiempoReproduccion}\n"
                f"Narrador: {self.__Narrador}\n")

    def mostrarDatos(self):
        super().mostrarDatos()
        self.importeVentaCD()

    def importeVentaCD(self):
        importe_venta= 0
        regalia = 0.10 * self.getPrecio()
        importe_venta = self.getPrecio() + regalia
        print(f"El importe de venta del CD es: ${importe_venta:.2f}")
