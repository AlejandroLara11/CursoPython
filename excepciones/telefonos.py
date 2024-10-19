import re
#Detectando un numero CABA y ocultandolo

texto = "Hola mi nombre es alejandro lara y mi numero es +52 777-41-342 +52 777-52-386"

pattern = r"\+52\s\d{3}-\d{2}-\d{3}"

remplazo = re.sub(pattern, "(numero oculto)", texto)

print(remplazo)