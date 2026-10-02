class Paciente:
    
    previsiones:set[str]= ["Fonasa", "Isapre", "Particular", "Otro"]

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
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El rut no puede estar vacio")
        self._rut = rut.strip().upper()

    ## property es para obtener el dato
    ## mientras que el setter es para guardar los datos
    @property
    def nombre(self)->str:
        return self._nombre
    @nombre.setter
    def nombre(self, nombre:str)->None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        self._nombre = nombre.strip().upper()

    @property
    def edad(self)->int:
        return self._edad
    @edad.setter
    def edad(self, edad:int)-> None:
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un numero positivo")
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        self._edad = edad

    @property
    def prevision(self)->str:
        return self._prevision
    @prevision.setter
    def prevision(self, prevision:str)->None:
        if not isinstance(prevision, str) or prevision.strip() not in self.prevision:
            raise ValueError("La prevision debe ser texto")
        prevision_limpio = prevision.strip().capitalize()
        if prevision_limpio not in self.previsiones:
            opciones = ', '.join(self.previsiones)
            raise ValueError(f"La prevision debe ser una de las siguientes: {opciones}")
        self._prevision = prevision_limpio

    def __str__(self)->str:
        return f"RUT: {self.rut}\nNombre: {self.nombre}\nEdad: {self.edad}\nPrevision: {self.prevision}"