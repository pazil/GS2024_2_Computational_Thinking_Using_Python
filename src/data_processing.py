import pandas as pd
import os

def carregar_dados(caminho):
    """
    Carrega os dados de consumo de um arquivo CSV.

    Args:
        caminho (str): Caminho para o arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados.
    """
    if os.path.exists(caminho):
        return pd.read_csv(caminho, parse_dates=["data"])
    else:
        raise FileNotFoundError(f"Arquivo {caminho} não encontrado.")

def salvar_dados(caminho, df):
    """
    Salva os dados atualizados no arquivo CSV.

    Args:
        caminho (str): Caminho para o arquivo CSV.
        df (pd.DataFrame): DataFrame a ser salvo.
    """
    df.to_csv(caminho, index=False)
