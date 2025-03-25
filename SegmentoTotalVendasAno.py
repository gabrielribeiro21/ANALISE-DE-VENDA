import pandas as pd
import matplotlib.pyplot as plt

# Qual o Total de Vendas Por Segmento e Por Ano?

# Carregar os dados
df = pd.read_excel("Sample-Superstore.xls")

# Garantir que 'Order Date' está como datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Criar coluna com o ano do pedido
df['Ano'] = df['Order Date'].dt.year

# Agrupar por Segmento e Ano, somando as vendas
vendas_segmento_ano = df.groupby(['Segment', 'Ano'])['Sales'].sum().reset_index()

# Exibir a tabela
# print(vendas_segmento_ano)

# Pivotar a tabela para ter os anos como colunas
tabela_pivot = vendas_segmento_ano.pivot(index='Ano', columns='Segment', values='Sales')

# Plotar gráfico
tabela_pivot.plot(kind='bar', figsize=(10, 6))
plt.title('Total de Vendas por Segmento e por Ano')
plt.xlabel('Ano')
plt.ylabel('Total de Vendas (R$)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
