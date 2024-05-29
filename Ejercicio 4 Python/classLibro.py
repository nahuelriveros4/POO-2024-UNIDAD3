from classPublicaciones import Publicaciones
from datetime import datetime
class Libro(Publicaciones):
    __Autor:str
    __FechaEdicion:int
    __CantidadPaginas: int
    def __init__(self, titulo, categoria, preciobase, autor="", fechaEdicion="", cantidadPaginas=0, tiempoReproduccion=0, narrador=""):
        super().__init__(titulo, categoria, preciobase, autor, fechaEdicion, cantidadPaginas, tiempoReproduccion, narrador)
        self.__Autor = autor
        self.__FechaEdicion = fechaEdicion
        self.__CantidadPaginas = cantidadPaginas

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Autor: {self.__Autor}\n"
                f"Fecha Edicion: {self.__FechaEdicion}\n"
                f"Cantidad de Paginas: {self.__CantidadPaginas}\n")
      

    def mostrarDatos(self):
        super().mostrarDatos()
        self.importeVentaLibro()

    
    def importeVentaLibro(self):
        importe_venta = 0
        año_actual = datetime.now().year
        antigüedad = año_actual - self.__FechaEdicion
        descuento = antigüedad * 0.01 * self.getPrecio()
        importe_venta = self.getPrecio() - descuento
        print(f"El importe de venta del libro es: ${importe_venta:.2f}")
