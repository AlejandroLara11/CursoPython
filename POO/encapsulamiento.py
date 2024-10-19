#atributo privado "_"
class Miclase:
    def __init__(self):
        self._atributo_privado = "valor"
    
    def _hablar(self):
        print("Helou kitty")

objeto = Miclase()
objeto._hablar()
print(objeto._atributo_privado)


#atributo muy muy privado "__"
class Miclase2:
    def __init__(self):
        self._atributo_privado = "valor"
    #Metodo muy privado
    def _presentarse(self):
        print("Helou")    
     
objeto2 = Miclase2()
objeto2._presentarse()
print(objeto2._atributo_privado)
