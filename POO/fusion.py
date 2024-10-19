class Personaje:
    def __init__(self, nombre, poder, velocidad):
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"Nombre: {self.nombre}, Fuerza: {self.poder}, Velocidad: {self.velocidad}"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nuevo_poder = self.poder + otro_pj.poder
        nueva_velocidad = self.velocidad + otro_pj.velocidad
        return Personaje(nuevo_nombre, nuevo_poder, nueva_velocidad)
    
def fusion(P1, P2):
        return P1+P2
    

    
cr7 = Personaje("Cristiano Ronaldo", 99, 86)
mbappe = Personaje("Mbappe", 85, 99)
print(cr7)
print(mbappe)
print(fusion(cr7, mbappe))