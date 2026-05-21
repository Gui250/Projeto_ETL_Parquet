import pandas as pd 
import os 
import glob
from utils_log import log_decorator

# uma função de extract que lida e consolida os jsons
@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# uma funcao que transforma
@log_decorator
def calcular_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame: 
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# uma funcao que da load em csv ou parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list): 
      for formato in format_saida:
                if formato == 'csv': 
                    df.to_csv("dados.csv", index=False)
                if formato == 'parquet': 
                    df.to_parquet("dados.parquet", index=False)

if __name__ == "__main__":
    pasta = 'data'
    dataframe = extrair_dados(pasta)
    dataframe_calculado = calcular_kpi_total_de_vendas(dataframe)
    formato_de_saida: list = ['csv', 'parquet']
    carregar_dados(dataframe_calculado, formato_de_saida)
