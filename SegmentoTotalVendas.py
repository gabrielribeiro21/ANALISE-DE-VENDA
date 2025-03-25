import pandas as pd
import matplotlib.pyplot as plt

# Qual Segmento Teve o Maior Total de Vendas?

# Carrega o arquivo Excel
df = pd.read_excel("Sample-Superstore.xls")

# Agrupar por segmento e somar as vendas
vendas_por_segmento = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

# Exibir gráfico de pizza
plt.figure(figsize=(8, 8))
cores = ['#66b3ff', '#99ff99', '#ff9999']
explode = [0.1 if i == 0 else 0 for i in range(len(vendas_por_segmento))]

plt.pie(
    vendas_por_segmento,
    labels=vendas_por_segmento.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=cores,
    explode=explode,
    shadow=True
)

plt.title('Participação de Vendas por Segmento')
plt.tight_layout()
plt.show()