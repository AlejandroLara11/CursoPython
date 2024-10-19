diccionario = dict(nombre = "Alejandro", apellido = "Lara", edad = 26)


numeros = list([2,5,8,10])


#Así solamente se obtienen las keys
for key in diccionario:
    print(key)

#aqui se utiliza el "items()" que devueve una tupla, (key:value)
for key, value in diccionario.items():
    print(f"La clave es: {key} y el valor en ese campo es: {value}")
    
    
    
#MAS ITERACIONES/CONTINUE
frutas = list(["fresa", "platano", "naranja", "ciruela", "durazno"])

for fruta in frutas:
    if fruta == "platano":
        continue  #Saltar
    print(fruta)
else:
    print("Ya no hay elementos para iterar.")
    
for fruta in frutas:
    if fruta == "platano":
        break  # en caso de coincidencia rompe el bucle y omite el else:
    print(fruta)
else:
    print("bucle terminado")
    
    
#iterar una cadena

cadena = "Bienvenido Alejandro"
for letra in cadena:
    print(letra)
    
    
#iterar en una sola linea
numeros_duplicados = [num**2 for num in numeros]
print(numeros_duplicados)

