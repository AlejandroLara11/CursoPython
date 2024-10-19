#CLASE PADRE (SUPER CLASE)
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando...")

#CLASE HIJO (SUB CLASE)
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    """
    def hablar(self):
        print("estoy trabajando...")
    """
    
roberto = Empleado("Roberto", 43, "mexicano", "Ingeniero", 45000)
print(roberto.trabajo)
roberto.hablar()