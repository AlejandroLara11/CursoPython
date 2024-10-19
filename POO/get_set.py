class Persona:
    def __init__(self, nombre, edad):
        #ATRIBUTO MUY PRIVADO
        self.__nombre = nombre
        #ATRIBUTO PRIVADO
        self._edad = edad
    #CREACION DEL GETTER QUE ME PERMITA ACCEDEER AL NOMBRE    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
alejandro = Persona("ALEJANDRO", 27)
#SE ACCEDE MEDIANTE EL GET INTERNAMENTE
nombre = alejandro.get_nombre()
print(nombre)
#print(alejandro.__nombre)    <-- ME VA A TIRAR ERROR
print(alejandro._edad)


#CAMBIAR EL VALOR DE UN ATRIBUTO MUY PRIVADO MEDIANTE SETTERS
alejandro.set_nombre("ELBICHO")
nombre = alejandro.get_nombre()
print(nombre)