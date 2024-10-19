#1 cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("datos.csv", names=["name", "lastname", "age"], na_values=["", " "])
print(df)

#convertir a string
df["age"] = df["age"].astype(str)
print(type(df["age"][0]))

#remplazar
df["name"].replace("axel", "julian", inplace = True)
print(df["name"])

#eliminar nulls
print(df)
df = df.dropna()   #axis = 1 son columnas, por defeto es axis = 0 o sea filas
print(df)

#eliminar duplicados
df = df.drop_duplicates()
print(df)

#guardar dataframe limpip
df.to_csv("datoslimpios.csv")