#Leer TXT con whit open
with open("texto_de_ale.txt", encoding="UTF-8") as archivo:  #EL ARCHIVO ESTÁ EN LA MISMA CARPETA
    print("Hola Mundo")
    #Leyendo archivo
    contenido = archivo.read()
    
    #Mostrar contenido
    print(contenido)  

