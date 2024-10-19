from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def realizar_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años.")
        

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def realizar_actividad(self):
        print(f"Estoy estudiando para ser {self.actividad}.")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def realizar_actividad(self):
        print(f"Estoy trabajando de {self.actividad}.")
    

    

alejandro = Estudiante("Alex", 27, "Masculino", "Programador")
dann = Trabajador("DANN", 32, "Masculino", "Ciberseguridad")
alejandro.presentarse()
alejandro.realizar_actividad()
dann.presentarse()
dann.realizar_actividad()