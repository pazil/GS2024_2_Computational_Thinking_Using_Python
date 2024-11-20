# **Sistema de Gerenciamento e Previsão de Energia Residencial**

Este projeto tem como objetivo prever o consumo mensal de energia elétrica residencial no Brasil utilizando redes neurais LSTM. A previsão do consumo energético é fundamental para o planejamento e uso eficiente dos recursos, possibilitando uma gestão mais eficaz das fontes de energia.

O sistema prevê o consumo futuro com base em dados históricos e fornece relatórios detalhados e gráficos para visualização. Ele também calcula a eficiência da energia solar disponível e estima a duração do estoque de energia solar.

---

## **Funcionalidades**

1. **Previsão do Consumo de Energia**:
   - Utiliza um modelo LSTM para prever o consumo dos próximos 12 meses com base nos últimos 12 meses de dados históricos.

2. **Gerenciamento de Fontes de Energia**:
   - Calcula o tempo de duração da energia solar disponível.
   - Indica o tempo necessário para recorrer à rede elétrica.

3. **Relatório de Eficiência Energética**:
   - Gera um relatório contendo:
     - Média de consumo real e previsto.
     - Erro médio absoluto.
     - Eficiência do modelo.

4. **Gráfico Interativo**:
   - Exibe o consumo histórico, a previsão do próximo mês e a duração do estoque de energia solar.

5. **Notebook de Treinamento**:
   - Contém o processo de tratamento, modelagem e avaliação do modelo LSTM.
   - Inclui métricas de desempenho, como MSE e RMSE.

---

## **Base de Dados**

- **Arquivo Utilizado**: `GS2024_2_Computational_Thinking_Using_Python/train_data/consumo_eletrico_brasil.csv`
- **Fonte dos Dados**: [Base dos Dados - Consumo Elétrico Residencial no Brasil](https://basedosdados.org/dataset/3e31e540-81ba-4665-9e72-3f81c176adad?table=b955feef-1649-428b-ba46-bc891d2facc2)
- **Descrição**:
  - Dados mensais do consumo de energia elétrica residencial no Brasil.
  - Inclui informações sobre consumo em MWh e número de consumidores.

---

## **Instalação**

### **Pré-requisitos**
- Python 3.8 ou superior
- Pacotes listados em `requirements.txt`
- Jupyter Notebook (para executar o notebook de treinamento)

### **Passos**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_projeto.git
   cd seu_projeto
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Certifique-se de que os seguintes diretórios existem:
   - `data/` para armazenar o arquivo `consumo_eletrico.csv`.
   - `models/` para armazenar o modelo LSTM treinado (`modelo_lstm.h5`).
   - `notebooks/` contendo o arquivo `GS2024_2_–_Redes_Neurais_e_Deep_Learning_ (2).ipynb`, com o treinamento e métricas do modelo.
   - `GS2024_2_Computational_Thinking_Using_Python/train_data/` contendo o arquivo `consumo_eletrico_brasil.csv`, utilizado para o treinamento do modelo.

---

## **Como Executar**

1. **Aplicação Streamlit**:
   - Inicie o sistema para gerenciamento de energia:
     ```bash
     streamlit run main.py
     ```
   - Acesse o sistema no navegador em [http://localhost:8501](http://localhost:8501).

2. **Notebook de Treinamento**:
   - Para treinar ou avaliar o modelo LSTM, execute o notebook:
     ```bash
     jupyter notebook notebooks/GS2024_2_–_Redes_Neurais_e_Deep_Learning_ (2).ipynb
     ```

---

## **Estrutura do Projeto**

```plaintext
📁 seu_projeto
├── 📁 data
│   └── consumo_eletrico.csv          # Dados históricos para Streamlit
├── 📁 models
│   └── modelo_lstm.h5                # Modelo LSTM treinado
├── 📁 notebooks
│   └── GS2024_2_–_Redes_Neurais_e_Deep_Learning_ (2).ipynb  # Notebook de treinamento
├── 📁 GS2024_2_Computational_Thinking_Using_Python
│   └── 📁 train_data
│       └── consumo_eletrico_brasil.csv  # Dados para treinamento da LSTM
├── 📁 src
│   ├── data_processing.py            # Funções para processamento de dados
│   ├── model.py                      # Funções para carregar e prever com o modelo
│   ├── visualization.py              # Funções para gráficos e relatórios
├── main.py                           # Aplicação Streamlit
├── requirements.txt                  # Dependências do projeto
└── README.md                         # Documentação do projeto
```

---

## **Relatório Gerado**

Ao clicar em **"Fazer Previsão e Gerar Relatório"**, o sistema gera o seguinte relatório:

```plaintext
Relatório de Eficiência Energética:
-----------------------------------
Média de Consumo Real: 450.00 W
Média de Consumo Previsto: 460.00 W
Erro Médio Absoluto: 10.00 W
Eficiência do Modelo: 97.83%
```

---

## **Treinamento do Modelo**

### **Arquitetura da Rede**
- **Modelo**: LSTM com:
  - 50 neurônios na camada LSTM.
  - Dropout de 0,2 para evitar overfitting.
  - Camada densa com ativação linear.
- **Otimizador**: Adam.
- **Função de Perda**: Mean Squared Error (MSE).

### **Avaliação**
- **Métricas**:
  - MSE: 753 bi.
  - RMSE: 867 mil.
- **Conclusão**:
  - O modelo apresentou dificuldades em capturar padrões sazonais e flutuações mensais, mas mostrou uma tendência média ao longo do tempo.

### **Notebook**
O arquivo `GS2024_2_–_Redes_Neurais_e_Deep_Learning_ (2).ipynb` contém:
- Tratamento dos dados.
- Pré-processamento e criação de sequências.
- Treinamento e avaliação do modelo.
- Previsão dos próximos 12 meses.

---

## **Tecnologias Utilizadas**

- **Linguagem:** Python
- **Machine Learning:** TensorFlow (LSTM)
- **Manipulação de Dados:** Pandas, NumPy
- **Visualização:** Matplotlib, Seaborn
- **Framework de Interface:** Streamlit
- **Treinamento do Modelo:** Jupyter Notebook
