import pandas as pd
import matplotlib.pyplot as plt

# Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

# Carrega o arquivo Excel
df = pd.read_excel("Sample-Superstore.xls")
# Filtra pela categoria 'Office Supplies'
filtro = df[df['Category'] == 'Office Supplies']

# Agrupa por cidade e soma as vendas
vendas_por_cidade = filtro.groupby('City')['Sales'].sum()

# Encontra a cidade com o maior valor de venda
cidade_top = vendas_por_cidade.idxmax()
valor_top = vendas_por_cidade.max()

# Exibe o resultado
print(f"🏆 A cidade com maior valor de venda de 'Office Supplies' é: {cidade_top}")
print(f"💰 Valor total vendido: R$ {valor_top:,.2f}")


