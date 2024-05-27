class Material:
    __Material: int
    __Caracteristicas:str
    __CantUtilizada: float
    __CostoAdicional:float

    def __init__(self, mater,carc,cant,costo):
        self.__Material = mater
        self.__Caracteristicas =carc
        self.__CantUtilizada = cant 
        self.__CostoAdicional = costo


    def __str__(self):
        return (f"Material: {self.__Material}\n"
                f"Carac: {self.__Caracteristicas}\n"
                f"Cant. Utilizada: {self.__CantUtilizada}\n"
                f"Costo Adicional: {self.__CostoAdicional}")
    
    def getCostoAdicional (self):
        return self.__CostoAdicional
    
    def getMaterial(self):
        return self.__Material
    
    def getCaracteristicas(self):
        return self.__Caracteristicas
    
    def getCant(self):
        return self.__CantUtilizada
    
   