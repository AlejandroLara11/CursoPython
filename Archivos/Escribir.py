with open("texto_de_ale.txt", "w", encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("JAJAJAJA")
    
    #Escribiendo dos lineas con writelines, esto TAMBIEN sobreescribe
    archivo.writelines(["Que paso master\n", "Misericordia\n"]) #Proceso inverso a readlines
    archivo.writelines(["no sé por qué puse eso\n", "Yo menos che\n"]) #Proceso inverso a readlines
    archivo.writelines(["Arriba las chivas\n","y el piojito alvarado"])