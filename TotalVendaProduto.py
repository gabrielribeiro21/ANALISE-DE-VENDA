import pandas as pd
import matplotlib.pyplot as plt

# Qual o Total de Vendas Por Data do Pedido?

# Carrega o arquivo Excel
df = pd.read_excel("Sample-Superstore.xls")  

# Garante que a coluna de data está no formato datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Mes'] = df['Order Date'].dt.strftime('%B')


# Agrupa por data e soma as vendas
vendas_por_data = df.groupby('Order Date')['Sales'].sum()

# Exibe as 5 primeiras linhas como exemplo
print(vendas_por_data.head())

meses_ordenados = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Agrupa por nome do mês e soma as vendas
vendas_por_mes = df.groupby('Mes')['Sales'].sum().reindex(meses_ordenados)

# Exibe o gráfico
plt.figure(figsize=(10, 6))
vendas_por_mes.plot(kind='bar', color='cornflowerblue')
plt.title('Total de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()