import pandas as pd

df = pd.read_csv("dados/SuperMarket-sales.csv")

print(df.info())

df = df.dropna()

df = df.rename(columns={
   "Invoice ID": "ID_Fatura",
    "Branch": "Filial",
    "City": "Cidade",
    "Customer type": "Tipo_Cliente",
    "Gender": "Genero",
    "Product line": "Linha_Produto",
    "Unit price": "Preco_Unitario",
    "Quantity": "Quantidade",
    "Tax 5%": "Imposto",
    "Total": "Total",
    "Date": "Data",
    "Time": "Hora",
    "Payment": "Pagamento",
    "cogs": "Custo",
    "gross margin percentage": "Margem_Bruta",
    "gross income": "Lucro_Bruto",
    "Rating": "Avaliacao"
})
      
       # 4. Traduzir valores de texto
df["Tipo_Cliente"] = df["Tipo_Cliente"].replace({
    "Member": "Membro",
    "Normal": "Normal"
})

df["Genero"] = df["Genero"].replace({
    "Male": "Masculino",
    "Female": "Feminino"
})

df["Pagamento"] = df["Pagamento"].replace({
    "Cash": "Dinheiro",
    "Credit card": "Cartão de Crédito",
    "Ewallet": "Carteira Digital"
})
# 5. Salvar arquivo traduzido
df.to_csv("dados/vendas_traduzidas.csv", index=False)

# 6. Criar coluna de faturamento
df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]

# 7. Criar resumo de faturamento por linha de produto
resumo_faturamento = (
    df.groupby("Linha_Produto")["Faturamento"]
    .sum()
    .reset_index()
)

# 8. Salvar resumo para Power BI
resumo_faturamento.to_csv(
    "dados/resumo_faturamento_por_produto.csv",
    index=False
)

# 9. Converter coluna Data para formato de data
df["Data"] = pd.to_datetime(df["Data"])

# 10. Criar coluna Mes_Ano
df["Mes_Ano"] = df["Data"].dt.to_period("M").astype(str)

# 11. Resumo de faturamento por mês
resumo_mensal = (
    df.groupby("Mes_Ano")["Faturamento"]
    .sum()
    .reset_index()
)

# 12. Salvar resumo mensal
resumo_mensal.to_csv(
    "dados/resumo_faturamento_mensal.csv",
    index=False
)

# 13. Ranking de produtos por faturamento
ranking_produtos = (
    df.groupby("Linha_Produto")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

# 14. Salvar ranking
ranking_produtos.to_csv(
    "dados/ranking_produtos.csv",
    index=False
)

print("Ranking de produtos criado com sucesso!")

