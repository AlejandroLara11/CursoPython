class Persona:
    #CONSTRUCTOR
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    #TODAS AS FUNCIONES QUE DEFINIMOS DENTRO DE UNA CLASE SE LLAMAN METODOS
    def llamar(self):
        print(f"Estas realizando una llamada a {self.name}...")
        
    def cortar(self):
        print(f"Terminaste la llamada al ingeniero {self.lastname}...")
        
        
persona1 = Persona("Alejandro", "Lara", 27)
persona1.llamar()
persona1.cortar()




