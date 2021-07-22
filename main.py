import pandas as pd
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