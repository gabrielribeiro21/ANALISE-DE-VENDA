import pandas as pd
import matplotlib.pyplot as plt

# Qual o Total de Vendas por Estado?

# Carrega o arquivo Excel
df = pd.read_excel("Sample-Superstore.xls")

# Agrupar por Estado e somar as vendas
vendas_por_estado = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)

# Exibir o gráfico
plt.figure(figsize=(10, 12))
vendas_por_estado.plot(kind='barh', color='darkorange')

plt.title('Top 10 Total de Vendas por Estado (Ordem Decrescente)')
plt.xlabel('Total de Vendas (R$)')
plt.ylabel('Estado')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
