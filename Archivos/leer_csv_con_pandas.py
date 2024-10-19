import pandas as pd

df = pd.read_csv("datos.csv", names=["name", "lastname", "age"])
df2 = pd.read_csv("datos.csv", names=["name", "lastname", "age"])
print("nombres de las columnas: ", df.columns, "\n")
#Obteniendo los datos de una columna espcifica
#print(df["name"])

#print(df)

df_orden_ascendente = df.sort_values('age')
df_orden_descendente = df.sort_values('age', ascending = False) #de mayor a menor con el false


print(df_orden_ascendente)
print(df_orden_descendente)


#CONCATENANDO LOS DOS ARCHIVOS
df_concatenado = pd.concat([df, df2])
print(df_concatenado)


#Accediendo a la primer fila
primer_fila = df.head(0)
print(primer_fila)


#Accediendo a las ultimas filas
ultimas_filas = df.tail(2)
print(ultimas_filas)


#accedendo a la cantidad de filas y columnas
filas_columnas = df.shape
print(filas_columnas)


filas_totales, columnas_totales = df.shape
print(f"El numero de filas es: {filas_totales}, y columnas hay: {columnas_totales} \n")


#obteniendo data estadistica del df
df_info = df.describe()
print(df_info)


#ACCEDIENDO A UN ELEMENTO ESPECÍFICO DEL DF CON LOC
elemento_especifico = df.loc[2, "age"]
print(elemento_especifico)


#ACCEDIENDO CON LOS INDICES (ILOC)
elemento_indices = df.iloc[2,2] #fila,columna
print(elemento_indices)

#ACCEDIENDO A TODAS LAS FILAS DE UNA COLUMNA
lastnames = df.iloc[:,1]
print(lastnames)

names = df.iloc[:,0]
print(names)

#ACCEDIENDO A LA FILA 3
fila3 = df.iloc[2,:]
print(fila3)


#accediendoo a filas con edad menor a 30
menor_30 = df.loc[df["age"] < 30, :]
print("Filas con edad menor a 30:")
print(menor_30)