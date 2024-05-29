class Publicaciones(object):
    __titulo:str
    __categoria:str
    __precioBase:float
    def __init__(self, titulo, categoria, preciobase, autor="", fechaEdicion="", cantidadPaginas = 0, tiempoReproduccion= 0.0, narrador=""):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precioBase = preciobase
    
    def mostrarDatos(self):
        print("\nDatos Pubclicacion")
        print(f"Titulo: {self.__titulo}")
        print(f"Categoria: {self.__categoria}")

    def __str__(self):
        return(f"Titulo: {self.__titulo}\n"
               f"Categoria: {self.__categoria}\n"
               f"Precio Base: {self.__precioBase}")
    
    def getPrecio(self):
        return self.__precioBase