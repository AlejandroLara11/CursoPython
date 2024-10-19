"""CREANDO UN DICCIONARIO CON dict()"""
tupla_vacia = tuple()
lista_vacia = list()
diccionario_vacio = dict()

diccionario = dict(nombre = "Alejandro", apellido = "Lara")
print(diccionario)
print(tupla_vacia)
print(lista_vacia)
print(diccionario_vacio)

#Las listas no pueden ser claves porque son mutables, pero las tuplas sí o
#Los frozenset también
diccionario = {("alejandro","lara") : "Empleado de sistemas"}
diccionario = {frozenset(["alejandro", "lara"]) : "Empleado de sistemas"}


#Creando diccionarios con fromkeys("Lo que vamos a iterar", "lo que vamos a igualar")
diccionario = dict.fromkeys(["Nombre", "Apellido", "Edad"], "vtgvar")
                                   #KEYS,              Valor por defecto

print(diccionario)