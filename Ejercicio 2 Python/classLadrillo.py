
class Ladrillo:
    __Alto =7
    __Largo = 25
    __Ancho = 15
    __Cantidad:int
    __id:int
    __kgMateriaPrima: float
    __costo: float
    __Material=list
    def __init__(self,cant,ide,kg,costo):
        self.__Cantidad = cant
        self.__id = ide
        self.__kgMateriaPrima = kg
        self.__costo = costo
        self.__Material=[]

    def __str__(self) -> str:
        return (f"Alto: {self.__Alto}\n"
                f"Largo: {self.__Largo}\n"
                f"Ancho: {self.__Ancho}\n"
                f"Cantidad: {self.__Cantidad}\n"
                f"ID: {self.__id}\n"
                f"KG Materia Prima: {self.__kgMateriaPrima}\n"
                f"Costo: {self.__costo}")
    

    def agregarMaterial(self,unMaterial):
        self.__Material.append(unMaterial)
        
    def printMaterial(self):
        for i in range(len(self.__Material)):
            print(f"{self.__Material[i]}")

    def getCostoAD(self):
        for i in range(len(self.__Material)):
           return self.__Material[i].getCostoAdicional()
        
    def getMat(self):
        for i in range(len(self.__Material)):
           return self.__Material[i].getMaterial()

    def getID(self):
        return self.__id
    
    def getCosto(self):
        return self.__costo
    
    def getMaterial(self):
        return self.__Material
    
    def getCant(self):
        return self.__kgMateriaPrima
    