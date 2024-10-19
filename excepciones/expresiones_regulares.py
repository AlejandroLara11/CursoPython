 #EXPRESIONES REGULARES

import re

texto = '''Hola maestro, esta es la cadena 1. como estas mi capitan?.
Esta es la linea 235 linea de texto aabb.
Y esta es la final (linea_3) definitiva mi capitan  abababbb
ab
'''

#Haciendo una busqueda simple
#resultado = re.findall("esta", texto)

#\d = Busca digitos numericos del 0 al 9

resultado = re.findall(r"\d", texto)
print(resultado)

#\D = Busca TODO MENOS digitos numericos del 0 al 9

resultado = re.findall(r"\D", texto)
print(resultado)

#\w = Busca caracteres alfanumericos [a-z, A-Z, 0-9, _]

resultado = re.findall(r"\w", texto)
print(resultado)

#\W = Busca TODO MENOS caracteres alfanumericos [a-z, A-Z, 0-9, _]

resultado = re.findall(r"\W", texto)
print(resultado)

#\s = Busca espacios en blando tabs y saltos de linea

resultado = re.findall(r"\s", texto)
print(resultado)

#\S = Busca TODO MENOS espacios en blando tabs y saltos de linea

resultado = re.findall(r"\S", texto)
print(resultado)

#. = BUSCA TODO MENOS SALTOS DE LINEA

resultado = re.findall(r".", texto)
print(resultado)

#\n = Busca los saltos de linea
resultado =re.findall(r"\n", texto)
print(resultado)

#\ = Cancela los caracteres especiales, cancelando la funcion del punto y vamos a buscar putos
resultado = re.findall(r"\.", texto)
print(resultado)

#Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)
print(resultado)

#^= Busca el comienzo de una linea
#flags = re.M activa la multilinea
resultado = re.findall(r"^Hola", texto, flags=re.M)
print(resultado)

#$ = Busca el final de una linea

resultado = re.findall(r"capitan$", texto)
print(resultado)

#{n} = Busca N cantidad de veces el valor a la izquierda
resultado = re.findall(r"\d{3}\s", texto) #tres numeros juntos y un espacio
print(resultado)


#{n,m} = Busca al menos n, como maximo m
resultado = re.findall(r"\d{1,4}", texto) #tres numeros juntos y un espacio
print(resultado)


#{n,m} = Busca cooincidencias de este lenguaje
resultado = re.findall(r"[ab]{2}", texto)
print(resultado)

# | = busca una cosa o la otra
resultado = re.findall(r"\d{2,4}|Hola", texto) #tres numeros juntos y un espacio
print(resultado)
