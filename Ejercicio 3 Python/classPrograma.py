class Programa:
    __Nombre:str
    __Codigo:str
    __Duracion: int
    __Matriculas : list
    def __init__(self,nom,cod,duracion):
        self.__Nombre = nom
        self.__Codigo = cod
        self.__Duracion = duracion
        self.__Matriculas = []

    def __str__(self) -> str:
        return (f"Nombre: {self.__Nombre}\n"
                f"Codigo: {self.__Codigo}\n"
                f"Duracion: {self.__Duracion}")
    
    def getNom(self):
        return self.__Nombre
    
    def getCod(self):
        return self.__Codigo
    
    def getDuracion(self):
        return self.__Duracion
    
    def addmatricula(self,unaMatricula):
        self.__Matriculas.append(unaMatricula)

    def mostrarEmp(self):
        print("\n-----Empleados matriculaos en el curso-----")
        for i in range(len(self.__Matriculas)):
            print(self.__Matriculas[i].getEmpleado())