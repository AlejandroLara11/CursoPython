#METODO DE RESOLUCION DE ORDEN

class A:
    def hablar(self):
        print("Hola desde CLASE A")

class C(A):
    def hablar(self):
        print("Hola desde CLASE C")

class B(C):
    def hablar(self):
        print("Hola desde CLASE B")
        
class D(B,C):
    pass

d = D()
d.hablar()

#asignarle o forzar un metodo de más arriba con loa atributos del objeto que ya tenemos
C.hablar(d)

print(D.mro())