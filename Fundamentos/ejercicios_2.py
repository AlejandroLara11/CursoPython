#Falto el profe y los pibes armaran la clase, el compi mayor sera el profe y el menor el asistente
#pedir el nombre y la edad de los compañeros
def obtener_lista_asistencia(cantidad):
    compa�eros = list([])
    cantidad_compis = cantidad
    for compis in range(cantidad_compis):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compa�ero = tuple([nombre, edad])
        compa�eros.append(compa�ero)
    compa�eros.sort(key=lambda parametros:parametros[1])
    #Se ordena por el segundo parametro (EDAD) de MENOS A MAS
    #KEY PERMITE AGREGAR UNA OPCION DE ORDENAMIENTO EN BASE A LAS NECESIDADES EN ESTE CASO SEGUNDO PARAMETRO
    asistente = compa�eros[0][0]
    #Accedemos a la primer tupla, al primer parametro (SU NOMBRE)
    profe = compa�eros[-1][0]
    #Accedemos a la ultima tupla, al primer parametro (SU NOMBRE)
    print(compa�eros)
    return asistente, profe

asistente, profesor = obtener_lista_asistencia(int(input("Ingrese el numero de asistentes: ")))
print(f"El profe sera {profesor} y su asistente por el dia de hoy sera {asistente}.")