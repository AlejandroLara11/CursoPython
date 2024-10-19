"""ENRUTAMIENTO"""
#Si el modulo estuviera dentro de una carpeta en la misma ruta
"""
import funciones_buenas.saludar as fb_saludar

print(fb_saludar.saludar("Lucas"))
"""
import sys
sys.path.append("C:\\Users\\dany1\\OneDrive\\Escritorio\\CursosPython\\funciones_buenas")
sys.path.append("C:\\Users\\dany1\\OneDrive\\Escritorio\\CursosPython\\Fundamentos")
print(sys.path)

import Funciones_propias as fp
import saludar as fb_saludar
print(fb_saludar.saludar("Alex"))
print(fp.saludar("Ingeniero", "m"))
contraseña, numero_utilizado = fp.crear_contraseña_random(25)
print(f"Su contraseña es: {contraseña}")