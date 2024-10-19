import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bigotes.csv") 
print(df)

#grafico de barras
sns.boxplot(x="category", y="value", data = df)
plt.show()
