import re

texto = "El dia de ayer se le vio caminando por las instalaciones."

sensurando = re.sub("[aeiou]", "*", texto)

print(sensurando)