archivo = open("C:\\Users\\dany1\\OneDrive\\Escritorio\\CursosPython\\Archivos\\texto_de_ale.txt", encoding="UTF-8")
#LEER ARCHIVO COMPLETO
#print(archivo.read())

#Leer lineas
lineas = archivo.readlines()
#print(lineas)

#Leer una sola linea
 
#linea = archivo.readline()
print(lineas)

archivo.close()
