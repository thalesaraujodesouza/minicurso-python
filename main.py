import pandas asimport pandas as pd
import openpyxl

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)

# faturamento por loja
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
#print(faturamento)

# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
#print(quantidade)

# ticket médio por produto em cada loja
ticketMedio = tabela_vendas[["ID Loja", "Produto", "Valor Unitário"]].groupby("ID Loja").median()
print(ticketMedio)
# enviar um email com o relatório pd
import openpyxl

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturamento por loja

# quantidade de produtos vendidos por loja

# ticket médio por produto em cada loja

# enviar um email com o relatório
