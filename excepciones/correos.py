import re

mail = "dany.11082011@gmail.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

resultado = re.match(pattern, mail)

if resultado:
    print("Correo valido")

else:
    print("correo invalido")