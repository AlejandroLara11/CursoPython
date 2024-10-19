import re

#texto para trabajar
texto = "El día 23/08/2024 se accedió a su cuenta"

#patron a encontrar
pattern = r"\d{2}/\d{2}/\d{4}"

#texto con el que se reemplazará el patron
replacement = "**/**/****"

#Reemplazando fechas
new_text = re.sub(pattern, replacement, texto)

#Imprimiendo nuevo texto
print("Texto modificado:", new_text)