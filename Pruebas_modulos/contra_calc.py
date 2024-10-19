"""practica"""
def pass_generator(num):
    int_to_str = str(num)
    first = int(int_to_str[0])
    cadena = "apuivn0rmcuio24u5ntg1o857ghn"
    n1 = first - 5
    n2 = first + 3
    n3 = first
    return f"Tu nueva contraseña es: {cadena[n1]}{cadena[n2]}{cadena[n3]}"

def calculadora(operacion, n1, n2):
    operacion = operacion.lower()
    if operacion == "suma":
        return n1+n2
    elif operacion == "resta":
        return n1-n2
    elif operacion == "multiplicacion":
        return n1*n2
    elif operacion == "division":
        return n1/n2
    else:
        return "Operacion invalida"