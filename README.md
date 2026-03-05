# Dashboard de Risco Cardíaco 🫀

Este projeto é um dashboard interativo desenvolvido em Python para visualizar dados sobre risco de doenças cardíacas.

O objetivo é analisar e explorar os dados de forma visual, utilizando gráficos e tabelas para facilitar a interpretação das informações.

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Matplotlib

## Funcionalidades

- Visualização do dataset completo
- Exibição das primeiras linhas do dataset
- Informações sobre número de linhas e colunas
- Distribuição de casos de doença cardíaca
- Gráfico mostrando a quantidade de pessoas com e sem doença cardíaca

## Estrutura do projeto

dashboard-risco-cardiaco
│
├── data
│   └── heart.csv
│
├── venv
│
├── app.py
│
└── README.md

## Como executar o projeto

1. Clone o repositório:

git clone https://github.com/sarahbubu/dashboard-risco-cardiaco.git

2. Entre na pasta do projeto:

cd dashboard-risco-cardiaco

3. Crie e ative o ambiente virtual:

python -m venv venv

4. Ative o ambiente virtual:

Windows:
venv\Scripts\activate

5. Instale as dependências:

pip install streamlit pandas matplotlib

6. Execute o dashboard:

streamlit run app.py
