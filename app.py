import streamlit as st
import pandas as pd

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