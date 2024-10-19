import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("incidencias.csv") 
print(df)

#grafico lineal
sns.lineplot(x="date", y="emergency", data = df)

#marcar un punto específica

plt.plot("08-ene", 9, "o", color = "r")


#moatrando el grafico
plt.show()