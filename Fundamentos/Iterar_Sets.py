#BUCLES
animales = {"gato", "perro", "loro", "cocodrilo"}
numeros = {3, 4, 0, 1}

"""
for animal in animales:
    print(f"Ahora la variable es igual a:  {animal}.")
"""

#Iterar más de una conjunto al mismo tiempo, tienen que se del mismo tamaño

for animal, cantidad in zip(animales,numeros):
    print(f"Recorriendo conjunto animales: {animal}")
    print(f"Recorriendo conjunto cantidad: {cantidad}")
    
for contador in range (5,15): #El primmero está incluido pero el ultimo no
    print(contador)
    
#FORMA INCORRECTA PORQUE NO FUNCIONA EN CONJUNTOS
"""
for num in range(len(numeros)):
    print(numeros[num])
    #print(num)
"""  
    
#FORMA CORRECTA (enumerate)
for indice, contenido in enumerate(numeros):
    #indice = num[0]
    #contenido = num[1]
    print(f"El indice es: {indice} y el valor en esa posicion es: {contenido}")
    
#USANDO EL FOR ELSE

for num in numeros:
    print(f"Ejecutando el último bucle, vaor actual: {num}")
else:
    print("Ya no hay contenido para iterar")
    