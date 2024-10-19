#PRINCIPIO DE RESPONSABIIDAD UNICA coding: utf-8 -*-
class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print(f"Haz movido el auto: {distancia} metros.")
        else:
            print("No hay combustible")
    
    def obtener_posicion(self):
        return self.posicion
        


class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    def agregar_combustible(self, litros_cargados):
        self.combustible += litros_cargados
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, litros_usados):
        self.combustible -= litros_usados
    
tanque = TanqueDeCombustible()
ibiza = Auto(tanque)

print(ibiza.obtener_posicion())
ibiza.mover(10)
print(ibiza.obtener_posicion())
ibiza.mover(20)
print(ibiza.obtener_posicion())
ibiza.mover(60)
print(ibiza.obtener_posicion())
ibiza.mover(100)
print(ibiza.obtener_posicion())
ibiza.mover(100)
print(ibiza.obtener_posicion())
