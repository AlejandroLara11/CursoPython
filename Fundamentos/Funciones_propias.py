#Creando una funcion simple
"""
def saludar():
    print("Hola Alejandro")

#EJECUTANDO LA FUNCION SIMPLE
saludar()
saludar()
saludar()
"""

#FUNCION CON PARAMETROS
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "f"):
        adjetivo = "minita"
        print(f"Hola {nombre}, cómo estas, {adjetivo}.")
    elif (sexo == "m"):
        print((f"Hola {nombre}, cómo estas, maquina"))
    else:
        print(f"Hola {nombre}, como estas, helicoptero apache 2314")
        
#saludar("Alejandro", "M")


#Crear una funcion que nos retorne valores y multiples valores (multiretorno)
def crear_contraseña_random(num):
    chars = "ypoipoikrdksvrw"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num-5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num


"""
contra, primer_numero = crear_contraseña_random(10)
frase = f"Tu contraseña generada es: {contra}, y se generó en base al numero: {primer_numero}"
print(frase)
"""
