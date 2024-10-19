#dos listas, una con nombres, otra con apellidos
nombres = ["daniel", "alejandro", "eric", "eden"]
apellidos = ["lara", "lopez", "williams", "hazard"]

with open("listacreada.txt", "w", encoding="UTF-8") as listacreada:
    listacreada.writelines("Los datos unidos son: \n")
    
    #listacreada.writelines(f"Nombre: {i}\nApellido: {j}\n--------------\n" for i,j in zip(nombres, apellidos))
    
    for i,j in zip(nombres, apellidos):
        listacreada.writelines(f"Nombre: {i}\nApellido: {j}\n------------\n")
    print(listacreada)
