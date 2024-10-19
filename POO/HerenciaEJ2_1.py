class Animal:
    def comer(self):
        print("Comiendo...")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando...")

class Ave(Animal):
    def volar(self):
        print("Volando...")
    
class Murcielago(Mamifero, Ave):
    pass
    
    
M = Murcielago()
M.comer()
M.amamantar()
M.volar()
print(Murcielago.mro())