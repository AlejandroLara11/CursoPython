#Las tuplas son para datos de solo lectura, ya que se almacenan diferente
#a una lista, para datos fijos son óptimas

#Funciona con tupla, listas, etc.
datos_tupla = ("Alejandro", "GOAT", "Lara", 26)
datos_lista = ["Daniel", "Piojito", "Alvarado", 28]

nombre, apodo, apellido, edad = datos_tupla
datos_congelados = frozenset(datos_lista)
print(datos_congelados)
#nombre, apodo, apellido, edad = datos_lista
print(nombre, apodo, apellido, edad)
print("------------------------------")

#Tupla con Tuple
tupla = tuple(["Dato1", "Dato2", "etc..."])


#Creando tupla sin parentesis
tupla = "dato 1", "dato 2", "datoN"


#Tupla de un solo dato
tupla = "Dato_N",


print(type(tupla))
print(tupla)
print("--------------------------------")



#CONJUNTOS
#Creando un conjunto con set() y recibe una lista de elementos
#NO MODIFICABLES, como tuplas.
conjunto = set(["Dato1", "Dato2", ("dato_en_tupla1", "dato_en_tupla2")])
print(conjunto)
print("--------------------")

#Meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Elemento1", "Elemento2"])
conjunto2 = {conjunto1, "Elemento3"}
print(conjunto2)
print("-----------------------------------")


#TEORIA DE CONJUNTOS
conjunto1 = {1, 3, 5, 7}
conjunto2 = {2,3,6}

#¿Conjunto 2 es un SUBCONJUNTO de conjunto 1?
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)

#¿Conjunto 1 es un SUPERCONJUNTO de conjunto 2?
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2
print(resultado)


#Será true en caso de que sean totalmente distintos los elementos, si hay uno igual, se vuelve false
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)