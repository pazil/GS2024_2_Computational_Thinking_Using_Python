import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

def normalizar_dados(df, scaler=None):
    """
    Normaliza os dados com MinMaxScaler.

    Args:
        df (pd.DataFrame): Dados de entrada.
        scaler (MinMaxScaler): Scaler existente ou None.

    Returns:
        tuple: Dados normalizados e o scaler.
    """
    if scaler is None:
        scaler = MinMaxScaler()
    df_normalizado = scaler.fit_transform(df[["consumo", "numero_consumidores"]])
    return df_normalizado, scaler

def fazer_previsao(df, modelo, n_steps):
    """
    Realiza a previsão com base nos últimos n_steps registros.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        modelo: Modelo LSTM carregado.
        n_steps (int): Número de passos para sequência.

    Returns:
        float: Previsão do consumo.
    """
    dados_normalizados, scaler = normalizar_dados(df)
    sequencia = np.array([dados_normalizados[-n_steps:]])
    previsao_normalizada = modelo.predict(sequencia)[0, 0]
    previsao = scaler.inverse_transform([[previsao_normalizada, 0]])[0, 0]
    return previsao
