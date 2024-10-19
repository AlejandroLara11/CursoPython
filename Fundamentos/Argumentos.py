#PARAMETRO *ARGS


"""ARGUMENTOS POSICIONALES"""
def suma(nombre, *numeros):
    return f"{nombre} la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Alejandro", 21, 12, 2, 4, 51)
print(resultado)




def frase(nombre, apellido, adjetivo = "Defecto"):
    return f"hola {nombre} {apellido}, sos un {adjetivo}"

"""FORZAR PARAMETROS (KEYWORDS ARGUMENTS)"""
frase_resultado = frase(apellido = "Lara", nombre = "Alejandro", adjetivo = "Maquina")
print(frase_resultado)

frase_resultado = frase(apellido = "Lara", nombre = "Alejandro")
print(frase_resultado)