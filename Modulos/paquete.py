"""Importar un paquete (carpeta ocn varios modulos) 
Al tener un archivo __init__ lo detecta como un paquete
y no un simple modulo"""

import paquete.saludar as ps
#print(type(paquete))
#print(paquete.__path__) #RUTA DEL PAQUETE
print(ps.saludar("Alex"))
#Nombre de la carpeta, Nombre del modulo(hoja), Nombre de la funcion llamada