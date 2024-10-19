#Ejercicio 1.2

frase = input("Decíme algo loco y te calculo cuánto tardarías si tuvieras que decirla: ")
separar_palabras = frase.split(" ")
cantidad_palabras = len(separar_palabras)
print(f"Dijisite {cantidad_palabras} palabras, y tardarías {cantidad_palabras/2} segundos en decirlo")
print(f"Dalto tardaría {cantidad_palabras /2 /1.3} segundos en decirlo")
if cantidad_palabras > 120:
    print("Pará flaco, tampoco te pedí una biblia")
