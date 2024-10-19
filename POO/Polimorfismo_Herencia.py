#POLIMORFISMO DE HERENCIA O SUBCLASES y ENLACE ESTATICO
class Animal:
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "MIAU..."
class Perro(Animal):
    def sonido(self):
        return "GUAU..."

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())
