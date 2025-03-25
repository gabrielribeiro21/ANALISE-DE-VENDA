# PROJETO2 - Análise Exploratória de Vendas

📊 Projeto de Análise de Dados em Python, com foco na exploração de informações de vendas para apoiar decisões estratégicas.

## 📁 Sobre

Este projeto realiza diferentes análises exploratórias com base em um conjunto de dados de vendas, utilizando a biblioteca **pandas** para manipulação de dados e **matplotlib** para visualizações.

Cada script Python no projeto representa uma etapa específica da análise.

---

## 🧪 Etapas da Análise

| Arquivo                       | Descrição                                                                         |
|-------------------------------|-----------------------------------------------------------------------------------|
| **BaseDeDesconto.py**         | Calcula quantas vendas receberiam 15% de desconto com base em uma regra de valor. |
| **CidadeValorVendaP.py**      | Identifica a cidade com o maior valor de venda na categoria "Office Supplies".    |
| **SegmentoTotalVendas.py**    | Verifica qual segmento teve o maior total de vendas.                              |
| **SegmentoTotalVendasAno.py** | Calcula o total de vendas por segmento em cada ano.                               |
| **Top10VendasProduto.py**     | Exibe as 10 cidades com maior valor de vendas.                                    |
| **VendasPorEstado.py**        | Calcula o total de vendas por estado, ordenando do maior para o menor.            |

---

## 🚀 Tecnologias utilizadas

- Python
- Pandas
- Matplotlib

---

## ⚙️ Como executar o projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/PROJETO2.git

# Acesse a pasta do projeto
cd PROJETO2

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Instale as dependências
pip install pandas matplotlib

# Execute o script desejado
python BaseDeDesconto.py
