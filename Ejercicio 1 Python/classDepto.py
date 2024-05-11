class Departamento:
    __idEdificio: int
    __idDpto:int
    __NomyAp:str
    __NumeroPiso:int
    __NumDpto:int
    __CantHabit:int
    __CantBaños:int
    __Sup:float
    def __init__(self,id1,id2,nom,piso,dpto,habit,baño,sup):
        self.__idEdificio = id1
        self.__idDpto = id2
        self.__NomyAp = nom
        self.__NumeroPiso=piso
        self.__NumDpto = dpto
        self.__CantHabit = habit
        self.__CantBaños = baño
        self.__Sup = sup
        
    def __str__(self):
        return (f"ID Edificio: {self.__idEdificio}\n"
                f"ID Departamento: {self.__idDpto}\n"
                f"Nombre y Apellido: {self.__NomyAp}\n"
                f"Número de Piso: {self.__NumeroPiso}\n"
                f"Número de Departamento: {self.__NumDpto}\n"
                f"Cantidad de Habitaciones: {self.__CantHabit}\n"
                f"Cantidad de Baños: {self.__CantBaños}\n"
                f"Superficie: {self.__Sup} m²")
    
    def getIDE(self):
        return self.__idEdificio
    
    def getIDD(self):
        return self.__idDpto
    
    def getNom(self):
        return self.__NomyAp
    
    def getSup(self):
        return self.__Sup
    
    def getPiso(self):
        return self.__NumeroPiso
    
    def getHabitacion(self):
        return self.__CantHabit
    
    def getBaños(self):
        return self.__CantBaños
    
    def getNumeroDpto(self):
        return self.__NumDpto
    
   