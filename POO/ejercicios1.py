class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"{self.nombre} alumno de {self.grado}, se encuentra estudiando actualmente con {self.edad} años.")

name = input("Cual es su nombre: ")
age = input("Que edad tiene: ")
degree = input("A que campo del CU pertenece: ")


estudiante1 = Estudiante(name, age, degree)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.estudiar()
        break