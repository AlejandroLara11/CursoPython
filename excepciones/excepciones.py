#Creando funcion que sume dos numeros
def sumar_dos():
    #iniciando bucle
    while True:
        #pidiendo dos numeros
        a = input("Ingrese el numero a: ")
        b = input("Ingrese el numero b: ")
        #tratando de sumar dos numeros
        try:
            #convirtiendo a enteros
            res = int(a) + int(b)
        #manejando tecleo de calquier cosa distinta a un numero
        except:
            print("solo se aceptan valores numericos")    
        #rompiendo bucle    
        else:
            break
        
        finally:
            print("manejo de excepcion finalizado")
        
    return res
    
print(sumar_dos())