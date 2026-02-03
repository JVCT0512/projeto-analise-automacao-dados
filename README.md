# 📊 Projeto de Análise e Automação de Dados – Supermercado

Este projeto foi desenvolvido com o objetivo de praticar **Análise de Dados**, utilizando **Python para automação e tratamento dos dados** e **Power BI para visualização e criação de dashboards**.

O foco foi transformar dados brutos de vendas em informações organizadas e fáceis de analisar.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (Pandas)
- **Power BI**
- **Git e GitHub**
- **CSV (dados estruturados)**

---

## 📁 Estrutura do Projeto
projeto-analise-automacao-dados/
│
├── dados/
│ ├── SuperMarket-sales.csv # Base de dados original
│ └── vendas_traduzidas.csv # Base tratada e traduzida
│
├── powerbi/
│ └── dashboard_supermercado.pbix # Dashboard no Power BI
│
├── python/
│ └── automacao-dados.py # Script de automação em Python

## ⚙️ Etapas do Projeto (Passo a Passo)

1. Importação dos Dados
Os dados de vendas foram importados a partir de um arquivo CSV utilizando a biblioteca **Pandas** no Python.
utilizei um dataset da kaggle

python
import pandas as pd
df = pd.read_csv("dados/SuperMarket-sales.csv")

2. Análise Inicial dos Dados

Foi utilizada a função df.info() para entender:

Quantidade de linhas, Tipos de dados e Valores nulos

Isso ajudou a identificar possíveis ajustes antes da análise.

3. Limpeza dos Dados

Foram removidos valores nulos para garantir maior qualidade na análise usando a função df = df.dropna()

4. Tradução das Colunas

Os nomes das colunas foram traduzidos do inglês para o português para facilitar o entendimento dos dados:
Exemplos:
Invoice ID → ID_Fatura

Product line → Linha_Produto

Total → Faturamento

5. Tradução dos Valores de Texto

Alguns valores categóricos também foram traduzidos:
Tipo de cliente: Member → Membro

Gênero: Male → Masculino

Forma de pagamento: Cash → Dinheiro

Isso facilitou para a análise e visualização.

6. Criação de Novas Informações

Foi criada a coluna Mês/Ano, permitindo análises temporais no Power BI: df["Mes_Ano"] = df["Data"].dt.to_period("M").astype(str)

7. Cálculo de Indicadores

Foram feitas análises como: Faturamento total, Faturamento por linha de produto,Faturamento mensal e Ranking de produtos por faturamento

Utilizando funções como groupby(), sum() e sort_values().

8. Exportação dos Dados Tratados

Após o tratamento, os dados foram salvos em um novo arquivo CSV:

df.to_csv("dados/vendas_traduzidas.csv", index=False)


Este arquivo foi utilizado no Power BI.

📊 Dashboard no Power BI

No Power BI, foram criadas as seguintes visualizações:

 Faturamento Total (KPI)
Faturamento por Linha de Produto
Faturamento Mensal
Ranking de Produtos por Faturamento

O dashboard foi organizado com foco em clareza, layout limpo e fácil leitura.

 Objetivo do Projeto

Este projeto foi desenvolvido para Praticar Python aplicado à análise de dados, Demonstrar automação de tratamento de dados, Criar dashboard no Power BI e Servir como projeto de portfólio para vagas de estágio em dados

 Autor:
João Victor Castilho
Estudante de Análise e Desenvolvimento de Sistemas
Interesse em Análise de Dados, Python, SQL e Power BI
