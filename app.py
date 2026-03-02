import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Dashboard de Risco Cardíaco🫀')

df = pd.read_csv('data/heart.csv')

st.subheader('Visualização dos dados')
st.dataframe(df)

st.subheader('Primeira 5 linhas')
st.write(df.head())

st.subheader('Informações do Dataset')
st.write('Numero de linhas:' , df.shape[0])
st.write('Numero de colunas:' , df.shape[1])
st.write('Colunas:' , df.columns)

st.subheader('Distribuição da Doença Cardíaca')
st.write(df['num'].value_counts())

df['Doença'] = df['num'].apply(lambda x: 0 if x == 0 else 1)

st.subheader('Distribuição Simplificada')
st.write(df['Doença'].value_counts())


st.subheader("Distribuição de Doença Cardíaca")

fig, ax = plt.subplots()
df["Doença"].value_counts().plot(
    kind="bar",
    ax=ax,
    color=["#4CAF50", "#E53935"]  
)

ax.set_title("Quantidade de Pacientes com e sem Doença Cardíaca")
ax.set_xlabel("Doença (0 = Não, 1 = Sim)")
ax.set_ylabel("Quantidade de Pacientes")

st.pyplot(fig)