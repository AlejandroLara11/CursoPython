#FUNCIONES 
#MAX Y MIN
numeros = tuple([4,2,4,6,7,7,3,4,50])
numeros1 = list([4,2,4,6,7,7,3,4,0])
numeros2 = set([4,2,4,6,7,7,3,4,50])
numeros3 = dict(nombre = "alex", edad = 26)
numero_mayor = max(numeros)
numero_menor = min(numeros)
print(numero_mayor)
print(numero_menor)


#ROUND
numero = round(19.756548, 2)
print(numero)

#retorna false si le pasamos 0, vacio, false, si no le pasamos nada.
res = bool(None)
print(res)

#Retorna True si todos los valores son verdaderos o distintos a 0, none, etc
resultado = all([21, "True", 23])
resultado = all(numeros)
resultado1 = all(numeros1)
resultado2 = all(numeros2)
resultado3 = all(numeros3)


print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)


#Suma los valores de un iterable con numeros
suma_total = sum(numeros)
print(suma_total)