#Metodos_Diccionarios

#Keys(tambien nos sirve para iterar) 
diccionario = {
    "nombre" : "Alejandro",
    "apellido" : "Lara",
    "edad" : 26
    }

claves = diccionario.keys()
print(claves)


#obteniendo un elemento con get()
valor_de_nombre = diccionario.get("nombre")
print(valor_de_nombre)

#Pop
diccionario.pop("nombre") #, otro elemento
print(diccionario)

#obteiendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)



#Eliminando todo el diccionario
#diccionario.clear()
#print(diccionario)