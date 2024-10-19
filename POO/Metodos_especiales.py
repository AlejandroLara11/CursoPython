class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Persona(nombre= {self.nombre}, edad= {self.edad})"
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre , nuevo_valor)
        
    
    
alejandro = Persona("ALEX", 27)
dann = Persona("DANN", 21)

nuevo_individuo = dann+alejandro
print(nuevo_individuo.nombre)
print(nuevo_individuo.edad)