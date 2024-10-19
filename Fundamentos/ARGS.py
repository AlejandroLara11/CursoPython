""" FORMA POCO OPTIMA

def suma(a, b):
    return a+b

print(suma(4, 5))

"""

#UTILIZANDO EL PARAMETRO ARGS
#EL PARAMETRO ARGS(*) SOLO SE PASA AL FINAL
def suma(nombre, *numeros):
    return f"Che {nombre}, el resultado de tu suma es: {sum(numeros)}"
    

resultado = suma("Alejandro", 5,7,9,2)
print(resultado)