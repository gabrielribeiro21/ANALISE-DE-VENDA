import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_excel("Sample-Superstore.xls")

# Aplica a regra de desconto com uma nova coluna
df['Desconto'] = df['Sales'].apply(lambda x: 0.15 if x > 1000 else 0.10)

# Conta quantas vendas receberiam 15% de desconto
vendas_com_15 = df[df['Desconto'] == 0.15]

# Resultado
qtd_15 = len(vendas_com_15)
print(f"🧾 Total de vendas que receberiam 15% de desconto: {qtd_15}")

df['Desconto'].value_counts().plot(kind='bar', color=['orange', 'green'])
plt.title('Quantidade de Vendas por Faixa de Desconto')
plt.xlabel('Percentual de Desconto')
plt.ylabel('Número de Vendas')
plt.xticks(ticks=[0, 1], labels=['10%', '15%'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
