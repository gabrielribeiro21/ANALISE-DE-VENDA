import pandas as pd
import matplotlib.pyplot as plt

# Quais São as 10 Cidades com Maior Total de Vendas?

# Carrega o arquivo Excel
df = pd.read_excel("Sample-Superstore.xls")  

# Agrupa por cidade, soma as vendas, ordena e pega top 10
vendas_por_cidade = (
    df.groupby('City')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Exibe gráfico de barras horizontais
plt.figure(figsize=(10, 6))
vendas_por_cidade.plot(kind='barh', color='steelblue')

plt.title('Top 10 Cidades com Maior Total de Vendas')
plt.xlabel('Total de Vendas (R$)')
plt.ylabel('Cidade')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()