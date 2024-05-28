class Matricula:
    __fecha:str
    __Empleado : object
    __Programa: object
    
    def __init__(self, fecha, empleado, program):
        self.__fecha = fecha
        self.__Empleado = empleado
        self.__Programa = program
        if empleado != None and program != None:
            self.__Empleado.addmatricula(self)
            self.__Programa.addmatricula(self)
      

    def __str__(self):
        return (f"Fecha: {self.__fecha}\n"
                f"Empleado: {self.__Empleado}\n"
                f"Programa: {self.__Programa}")
    

    def getPrograma(self):
        return self.__Programa
    
    def getEmpleado(self):
        return self.__Empleado.getNom()