contraseñaGuardada = "Admin1234"
ContraseñaIngresada = input("Ingrese una contraseña: ")
if ContraseñaIngresada == contraseñaGuardada:
    print("Iniciando Sesión...")
else:
    print("Contraseña incorrecta, intente de nuevo.")
    
    
    
ingresoMensual = int(input("Digite su ingreso mensual estimado: "))

if ingresoMensual > 100000:
    print("Su ingreso mensual es bueno")
elif ingresoMensual >= 10000:
    print("Su ingreso mensual es medio")
elif ingresoMensual > 1000:
    print("Su ingreso mensual es malo")
else:
    print("No alcanza el ingreso mensual minimo")