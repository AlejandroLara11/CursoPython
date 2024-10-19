#Falto el profe y los pibes armaran la clase, el compi mayor sera el profe y el menor el asistente
#pedir el nombre y la edad de los compaÃ±eros
def obtener_lista_asistencia(cantidad):
    compañeros = list([])
    cantidad_compis = cantidad
    for compis in range(cantidad_compis):
        nombre = input("Ingrese el nombre del compaÃ±ero: ")
        edad = int(input("Ingrese la edad del compaÃ±ero: "))
        compañero = tuple([nombre, edad])
        compañeros.append(compañero)
    compañeros.sort(key=lambda parametros:parametros[1])
    #Se ordena por el segundo parametro (EDAD) de MENOS A MAS
    #KEY PERMITE AGREGAR UNA OPCION DE ORDENAMIENTO EN BASE A LAS NECESIDADES EN ESTE CASO SEGUNDO PARAMETRO
    asistente = compañeros[0][0]
    #Accedemos a la primer tupla, al primer parametro (SU NOMBRE)
    profe = compañeros[-1][0]
    #Accedemos a la ultima tupla, al primer parametro (SU NOMBRE)
    print(compañeros)
    return asistente, profe

asistente, profesor = obtener_lista_asistencia(int(input("Ingrese el numero de asistentes: ")))
print(f"El profe sera {profesor} y su asistente por el dia de hoy sera {asistente}.")