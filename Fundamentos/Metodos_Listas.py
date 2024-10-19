#Metodos de listas
lista = list(["Hola", "Dann", 26, "Ingenieri�a", True])

#Numero de elementos en la lista
resultado = len(lista)
print(resultado)

#APPEND
lista.append(35)
resultado = lista
print(resultado)

#INSERT
lista.insert(0, "Bienvenido")
print(lista)

#Extend
lista.extend([False, 2023])
print(lista)

#Pop/eliminando por el indice
lista.pop(-1)
print(lista)

#Remove, por su valor
lista.remove("Dann")
print(lista)

lista2 = list([23, 45, 21, 85, 23, True, 34, False, 5])
#Sort/Ordenar elementos de menor a mayor por defecto
lista2.sort()
print(lista2)

#Reverse invierte el orden y se puede utiizar así
#lista2.sort(reverse = True)
#o así
lista2.reverse()
print(lista2)

#Verificando si un elemento se encuentra en la lista:
resultado = lista.index("Hola")
print(resultado)
letra = lista[1].find("l")
print(letra)

print(lista)

#Clear, limpia toda la lista