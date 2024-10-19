class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, y tengo {self.edad} años.")
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, semestre):
        super().__init__(nombre, edad)
        self.semestre = semestre
    def grado(self):
        print(f"Voy en {self.semestre} grado.")
        
Alex = Estudiante("Alejandro", 27, "decimo")
Alex.presentarse()
Alex.grado()
 