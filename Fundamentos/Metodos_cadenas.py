
#Metodos con cadenas
cadena1 = "ArribalasChivas"
cadena2 = "Hala Madrid"
cadena3 = "1258"
cadena4 = "LAFD"
#print(dir(cadena1)) #Ver algunos metodos que se le pueden aplicar
#resultado = dir(cadena2)

#Mayusculas o minusculas
resultado = cadena1.upper()
resultado = cadena2.lower()

#Encuentra la primer aparicion, y regresa -1 si no la enuentra
resultado = cadena1.find("a")

#Index en caso de no encontrar coincidencias lanza una excepcion
resultado = cadena2.index("a")

#Si es numerico devuelve true
resultado = cadena3.isnumeric()
#Si es alfanumerico devuelve true
resultado = cadena4.isalpha()


#Devuelve la cantidad de coincidencias
resultado = cadena1.count("a")


#Cantidad de caracteres, no es un metodo, es una función
resultado = len(cadena2)

#¿Inicia/termina con...?
resultado = cadena1.startswith("A") & cadena2.startswith("H")
resultado = cadena4.endswith("FD")

#Remplaza
resultado = cadena1.replace("Arriba", "Nuevo Campeón")




print(resultado)

