import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dispercion.csv") 
print(df)

#grafico de barras
sns.scatterplot(x="dias", y="cantidad", data = df)
plt.show()
