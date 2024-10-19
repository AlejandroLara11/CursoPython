with open("texto_de_ale.txt", "a", encoding="UTF-8") as archivo:
    for i in range(10):
        archivo.write(f"Agregando linea {i} al texto\n")