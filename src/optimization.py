def decidir_fonte(consumo_previsto, tarifa_rede, geracao_solar, custo_solar):
    """
    Decide a melhor fonte de energia (solar ou rede) com base nos custos.

    Args:
        consumo_previsto (float): Consumo de energia previsto (W).
        tarifa_rede (float): Tarifa atual da rede elétrica (R$/W).
        geracao_solar (float): Geração solar disponível (W).
        custo_solar (float): Custo da energia solar (R$/W).

    Returns:
        str: 'Solar' ou 'Rede' indicando a fonte de energia selecionada.
    """
    custo_rede = consumo_previsto * tarifa_rede
    custo_total_solar = custo_solar * consumo_previsto

    if geracao_solar >= consumo_previsto and custo_total_solar < custo_rede:
        return 'Solar'
    else:
        return 'Rede'
