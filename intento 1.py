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
def nombre(self)->str