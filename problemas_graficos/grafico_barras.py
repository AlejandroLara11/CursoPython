import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dann_ingresos.csv") 
print(df)

#grafico de barras
sns.barplot(x="fuente", y="ingresos", data = df)
plt.show()

total_ingresos = df["ingresos"].sum()
print(f"el total de ingresos es de: {total_ingresos}")