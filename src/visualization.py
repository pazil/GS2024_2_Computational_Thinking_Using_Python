import matplotlib.pyplot as plt
import numpy as np

def gerar_relatorio(real, previsto):
    """
    Gera um relatório de eficiência energética baseado nos valores reais e previstos.

    Args:
        real (list): Consumo real (W).
        previsto (list): Consumo previsto (W).

    Returns:
        str: Relatório formatado.
    """
    erro = np.abs(np.array(real) - np.array(previsto))
    eficiencia = (1 - (erro.mean() / np.mean(real))) * 100

    relatorio = f"""
    Relatório de Eficiência Energética:
    -----------------------------------
    Média de Consumo Real: {np.mean(real):.2f} W
    Média de Consumo Previsto: {np.mean(previsto):.2f} W
    Erro Médio Absoluto: {erro.mean():.2f} W
    Eficiência do Modelo: {eficiencia:.2f}%
    """
    return relatorio

def plotar_consumo(real, previsto, datas, meses_duracao_solar, energia_solar_disponivel):
    """
    Plota o consumo do último mês e a previsão para o próximo mês.

    Args:
        real (list): Consumo do último mês (kWh).
        previsto (list): Previsão para o próximo mês (kWh).
        datas (list): Datas correspondentes ao último mês e ao próximo mês.
        meses_duracao_solar (float): Duração estimada do estoque de energia solar (em meses).
        energia_solar_disponivel (float): Energia solar disponível (kWh).

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))

    # Plotar o consumo do último mês
    plt.bar([datas[0]], real, label="Último Mês", color="blue", width=20)

    # Plotar a previsão para o próximo mês
    plt.bar([datas[1]], previsto, label="Próximo Mês (Previsto)", color="orange", width=20)

    # Adicionar linha indicando o estoque de energia solar
    plt.axhline(y=energia_solar_disponivel, color="green", linestyle=":", label=f"Estoque Solar ({energia_solar_disponivel} kWh)")

    # Indicar o ponto onde o estoque de energia solar se esgota
    if meses_duracao_solar >= 1:
        plt.axvline(x=datas[1], color="red", linestyle="--", label="Estoque Solar Dura Totalmente")
    else:
        plt.axvline(x=datas[1], color="red", linestyle="--", label="Estoque Solar Insuficiente")

    plt.xlabel("Data")
    plt.ylabel("Consumo (kWh)")
    plt.title("Consumo do Último Mês e Previsão para o Próximo Mês")
    plt.legend()
    plt.grid(True)
    plt.show()
