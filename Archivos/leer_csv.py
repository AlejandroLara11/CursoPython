import csv

with open("datos.csv") as archivo:
    print("Datos cargados correctamente...")
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
        