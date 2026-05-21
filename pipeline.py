from etl import extrair_dados, calcular_kpi_total_de_vendas, carregar_dados

pasta = 'data'
formato_saida = ["csv"]

df = extrair_dados(pasta)
df = calcular_kpi_total_de_vendas(df)
carregar_dados(df, formato_saida)