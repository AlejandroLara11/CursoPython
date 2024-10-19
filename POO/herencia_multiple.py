class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, matricula, carrera):
        super().__init__(nombre, edad, nacionalidad)
        self.matricula = matricula
        self.carrera = carrera
    def estudiar(self):
        print("Estudiando")
        
        
class Artista:
    def __init__(self, skill):
        self.skill = skill
    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.skill}"
        

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, skill, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, skill)
        self.salario = salario
        self.empresa = empresa
        
    def mostrar_habilidad(self):
        return "no se hacer nada"  
   
    def presentarse(self):
        #print(f"Hola mi nombre es {self.nombre}, {self.mostrar_habilidad()} y trabajo para {self.empresa}") 
        #LLAMA A SU PROPIO METODO
        
        print(f"Hola mi nombre es {self.nombre}, {super().mostrar_habilidad()} y trabajo para {self.empresa}")
        #LLAMA AL METODO HEREDADO
      
        
Alejandro = EmpleadoArtista("Alejandro", 27, "Mexicano", "Programar", 45000, "Amazon")
Alejandro.presentarse()

#EMPLEADO HEREDA DE ARTISTA?
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

#INSTANCIA(OBJETO) DE?
instancia = isinstance(Alejandro, EmpleadoArtista)
print(instancia)