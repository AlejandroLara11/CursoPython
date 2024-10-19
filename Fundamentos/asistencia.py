def lista(cantidad):
    asistentes = list([])
    for compi in range(cantidad):
        nombre = input("Dime tu nombre: ")
        edad = int(input("Digita tu edad: "))
        asistentes.append((nombre,edad))
    asistentes.sort(key = lambda param:param[1] , reverse=True)
    profe = asistentes[0][0]
    ayudante = asistentes[-1][0]
    return profe, ayudante

profesor, ayudante = lista(int(input("Digite el numero de asistentes del dia de hoy: ")))
print(f"El profesor el dia de hoy sera: {profesor}, y su asistente sera: {ayudante}")