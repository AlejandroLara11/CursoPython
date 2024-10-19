lista = ["Hola", "Alejandro", 26, "EdoMex", "Hola"]
print(lista)
lista[2] = "Daniel"
print(lista)
#Las listas son modificables

tupla = ("Alfonso", 36, "Vallarta", 36)
print(tupla)
#tupla[1]=21 Las tuplas no son modificables

#Conjunto "set", se pueden eliminan duplicados
#no se pueden acceder directo por indice, solamente iterar sobre el
conjunto = {"Hola", "Alejandro", 26, "EdoMex", "Hola"}
print(conjunto)


diccionario = {
    "Bajo" : "No aceptar",
    "Medio" : "50/50",
    "Alto" : "Aceptar"
    }

print(diccionario["Alto"])
print(diccionario["Medio"])

