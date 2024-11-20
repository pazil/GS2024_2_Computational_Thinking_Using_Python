import streamlit as st
from src.data_processing import carregar_dados, salvar_dados
from src.model import fazer_previsao
from src.visualization import plotar_consumo
from tensorflow.keras.models import load_model
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Configurações iniciais
caminho_arquivo = "data/consumo_eletrico.csv"
modelo_caminho = "models/modelo_lstm.h5"

# Carregar dados e modelo
df = carregar_dados(caminho_arquivo)

# Garantir que a coluna "data" seja datetime
df["data"] = pd.to_datetime(df["data"], errors='coerce', format='%Y-%m-%d %H:%M:%S.%f')

# Verificar se há valores inválidos após a conversão
if df["data"].isna().any():
    st.error("Alguns valores na coluna 'data' não puderam ser convertidos para datetime. Verifique o arquivo.")
    st.stop()

# Carregar o modelo
try:
    modelo = load_model(modelo_caminho)
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")
    st.stop()

# Exibir dados existentes
st.title("Sistema de Gerenciamento de Energia")
st.subheader("Dados Históricos")
df_exibicao = df.assign(consumo=lambda x: x["consumo"] * 1000)  # Converter para kWh
st.write(df_exibicao.tail(12))

# Entrada de novos dados
st.subheader("Inserir Novo Registro")
data = st.date_input("Data")  # O usuário insere apenas a data
horario_atual = datetime.datetime.now().time()  # Pega o horário atual
data_completa = datetime.datetime.combine(data, horario_atual)  # Combina a data com o horário atual

consumo_kwh = st.number_input("Consumo (kWh)", min_value=0.0, step=1.0)  # Entrada em kWh
numero_consumidores = st.number_input("Número de Consumidores", min_value=1, step=1)

if st.button("Adicionar Registro"):
    consumo_mwh = consumo_kwh / 1000  # Converter para MWh antes de salvar
    novo_registro = pd.DataFrame({
        "data": [data_completa],  # Adicionar a data completa
        "consumo": [consumo_mwh],
        "numero_consumidores": [numero_consumidores]
    })
    df = pd.concat([df, novo_registro], ignore_index=True)
    salvar_dados(caminho_arquivo, df)
    st.success(f"Registro adicionado com sucesso! Data registrada: {data_completa}")

# Configurações do usuário para energia
st.sidebar.header("Configurações de Energia")
energia_solar_disponivel_kwh = st.sidebar.number_input("Energia Solar Disponível (kWh)", min_value=0.0, value=100.0, step=1.0)
energia_solar_disponivel_mwh = energia_solar_disponivel_kwh / 1000

if energia_solar_disponivel_mwh <= 0:
    st.error("A energia solar disponível deve ser maior que 0.")
    st.stop()

# Previsão e gráfico para último e próximo mês
if st.button("Fazer Previsão e Gerar Relatório"):
    if len(df) >= 12:
        try:
            consumo_ultimo_mes_kwh = df["consumo"].iloc[-1] * 1000
            data_ultimo_mes = df["data"].iloc[-1]

            previsao_mwh = fazer_previsao(df.tail(12), modelo, n_steps=12)
            previsao_kwh = previsao_mwh * 1000
            data_proximo_mes = data_ultimo_mes + pd.DateOffset(months=1)

            meses_duracao_solar = energia_solar_disponivel_mwh / previsao_mwh

            st.subheader("Relatório de Energia")
            st.write(f"Consumo do último mês ({data_ultimo_mes.strftime('%Y-%m-%d %H:%M:%S.%f')}): **{consumo_ultimo_mes_kwh:.2f} kWh**")
            st.write(f"Previsão de consumo para o próximo mês ({data_proximo_mes.strftime('%Y-%m-%d')}): **{previsao_kwh:.2f} kWh**")
            st.write(f"Tempo de duração da energia solar: **{meses_duracao_solar:.2f} meses**")

            st.subheader("Consumo do Último Mês e Previsão")
            plotar_consumo([consumo_ultimo_mes_kwh], [previsao_kwh], [data_ultimo_mes, data_proximo_mes], meses_duracao_solar, energia_solar_disponivel_kwh)
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Erro ao gerar a previsão: {e}")
    else:
        st.error("São necessários pelo menos 12 registros para gerar a previsão.")
