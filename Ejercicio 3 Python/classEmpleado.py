class Empleado:
    __NomyAp: str
    __IDempleado: int
    __Puesto:str
    __Matriculas:list
    def __init__(self,nom,ide,puesto):
        self.__NomyAp = nom
        self.__IDempleado = ide
        self.__Puesto = puesto
        self.__Matriculas = []

    
    def __str__(self) -> str:
        return (f"Nombre y Apellido: {self.__NomyAp}\n"
                f"ID Empleado: {self.__IDempleado}\n"
                f"Puesto: {self.__Puesto}")
    

    def addmatricula(self,unaMatricula):
        self.__Matriculas.append(unaMatricula)

    def printMatricula(self):
        for i in range(len(self.__Matriculas)):
            print(self.__Matriculas[i])

    def mostrarDuracion(self):
        for i in range(len(self.__Matriculas)):
            print(f"\n{self.__Matriculas[i].getPrograma()}")

    def mostrarMatriculas(self):
        if len(self.__Matriculas) == 0:
                print(f"El empleado {self.getNom()} no esta matriculado en ningun programa")

    def getNom(self):
        return self.__NomyAp
    
    def getID(self):
        return self.__IDempleado
    
    def getPuesto(self):
        return self.__Puesto