class paciente:
    def __init__(self,rut:str,nombre:str,edad:int,prevision:str):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision

@property
def rut(self)->str:
    return self._rut 
## el atributo por si solo es publico, con un _ es privado y con 2 es seguro
@rut.setter
def rut(self, rut:str)->None:
    self._rut = rut

## property es para obtener el dato
## mientras que el setter es para guardar los datos
@property
def nombre(self)->str:
    return self.nombre
@nombre.setter
def nombre(self, nombre:str):
    self._nombre = nombre

@property
def edad(self)->int:
    return self.edad
@edad.setter
def edad(self, edad:int)-> None:
    self._edad = edad

@property
def prevision(self)->str:
    return self.prevision
@prevision.setter
def prevision(self, prevision:str):
    self._prevision = prevision